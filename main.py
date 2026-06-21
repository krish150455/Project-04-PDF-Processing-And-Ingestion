#Till now, we've been using .txt files. But in real world, we've pdfs and text needs to be extracted from it.
#Extraction of text from pdf to further convert it into embeddings is known as, "DOCUMENT INGESTION."

#A real RAG System has 2 pipelines - online and offline.
#Online pipeline deals with query embeddings, retrieving matches,LLM and all
#Offline pipeline is what we're building now which involves extracting texts, converting them to chunks
#then to embeddings and finally storing them.

from PyPDF2 import PdfReader

#TO GET NO OF PAGES, TEXT IN EACH PAGE:
reader = PdfReader("pdfs/pages.pdf")
page = reader.pages[0]
print(page.extract_text())
print("No of pages:", len(reader.pages))

#TO GET METADATA:
meta = reader.metadata
print(meta.author) #so on so many parameters are available like author, creator, producer etc

pdf_data=[]

for i in range(1,len(reader.pages)+1):
    dict1={}
    dict1["page"]=i
    dict1["text"]=reader.pages[i-1].extract_text()
    dict1["source"]="pages.pdf"
    dict1["char_count"]=len(reader.pages[i-1].extract_text())
    if len(reader.pages[i-1].extract_text())==0:
        dict1["status"]="empty"
    elif len(reader.pages[i-1].extract_text())<10:
        dict1["status"]="suspicious"
    else:
        dict1["status"]="good"
    pdf_data.append(dict1)
print(len(pdf_data))


#BUILDING A DOCUMENT INGESTION SYSTEM:

def load_pdf(name: str):
    reader = PdfReader(name)
    print("No of pages in:",name,reader.pages)
    return reader

def extract_pages(reader,source:str):
    data=[]
    for i in range(1, len(reader.pages)+1):
        dict1={}
        dict1["page"]=i
        dict1["text"]=reader.pages[i-1].extract_text()
        dict1["source"]= source
        dict1["page"]= i
        data.append(dict1)
    return data

def extract_metadata_quality(reader,data):
    meta = reader.metadata
    for item in data:
        item["author"]=meta.author
        item["creator"] = meta.creator
        item["producer"] = meta.producer
        item["subject"] = meta.subject
        item["title"] = meta.title
        if len(item["text"]) == 0:
            item["status"] = "empty"
        elif len(item["text"]) < 10:
            item["status"] = "suspicious"
        else:
            item["status"] = "good"
    return data

def ingest_pdf(path: str):
    reader = load_pdf(path)
    data = extract_pages(reader, path)
    nextdata = extract_metadata_quality(reader, data)
    return nextdata