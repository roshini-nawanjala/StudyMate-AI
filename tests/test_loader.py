from utils.file_loader import PDFLoader

loader = PDFLoader()

text = loader.extract_text("data/uploads/lecture1.pdf")

print(text[:1000])