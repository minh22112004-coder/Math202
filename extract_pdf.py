import pdfplumber
import os

pdf_files = [
    "1727253773.pdf",
    "Graph Traversal.pptx.pdf",
    "Lec12.pptx.pdf",
    "Lec13.pdf",
    "Topological Sorting .pptx.pdf",
    "Tree.pptx.pdf"
]

output_dir = "extracted_content"
os.makedirs(output_dir, exist_ok=True)

for pdf_file in pdf_files:
    print(f"\nĐang xử lý: {pdf_file}")
    try:
        with pdfplumber.open(pdf_file) as pdf:
            text_content = []
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text:
                    text_content.append(f"=== Trang {i+1} ===\n{text}\n")
            
            # Lưu nội dung vào file text
            output_file = os.path.join(output_dir, f"{os.path.splitext(pdf_file)[0]}.txt")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(text_content))
            
            print(f"✓ Đã trích xuất {len(pdf.pages)} trang từ {pdf_file}")
    except Exception as e:
        print(f"✗ Lỗi khi xử lý {pdf_file}: {str(e)}")

print("\n✓ Hoàn thành! Các file text đã được lưu trong thư mục 'extracted_content'")
