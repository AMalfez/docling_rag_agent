from docling.document_converter import DocumentConverter
from docling.chunking import HybridChunker
from embedding import create_chroma_db
import os
from dotenv import load_dotenv
load_dotenv()

converter = DocumentConverter()

paths = [
    './sample_data/alfez_mansuri_resume.pdf',
    './sample_data/Basic_presentation.pptx',
    './sample_data/tweeter_post_generator.md',
    './sample_data/Welcome_to_Word.docx',
]

chunker = HybridChunker()

print("Initializing ChromaDB collection 'test_db'...\n")
db = create_chroma_db("test_db")

print("Adding documents to ChromaDB collection 'test_db'...\n")
for path in paths:
    doc = converter.convert(path).document
    chunk_itr = chunker.chunk(dl_doc=doc)
    for i, chunk in enumerate(chunk_itr):
        ids = [f"{os.path.basename(path)}_chunk_{i}"]
        metadatas = [{"source": path}]
        db.add(
            documents=chunker.contextualize(chunk=chunk),
            metadatas=metadatas,
            ids=ids
        )

print("Data added to ChromaDB collection 'test_db'\n")
