from PyPDF2 import PdfReader, PdfWriter
import uuid
import env

def generate_filename () : return uuid.uuid4().hex[:10].upper()

def rotate_and_save(f, page_numbers, angle):
    try:
        reader = PdfReader(f)
        writer = PdfWriter()
        
        k = 0
        page_numbers = page_numbers.replace(" ", "").split(",")
        n_pages = len(page_numbers) - 1

        for index, page in enumerate(reader.pages):
            if k <= n_pages:
                if index == int(page_numbers[k]) - 1:
                    k += 1
                    page = page.rotate_clockwise(int(angle))
            writer.add_page(page)
            
        output_filename = generate_filename()
        output_dir = env.PDF_OUTPUT_DIR + output_filename + ".pdf"
        with open(output_dir, "wb") as pdf_out:
            writer.write(pdf_out)
        
        return env.FILE_URL + output_filename + ".pdf"
    
    except Exception as e:
        return False