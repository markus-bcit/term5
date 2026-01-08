import os
import subprocess
import zipfile
import xml.etree.ElementTree as ET

def extract_text_from_pdf(pdf_path):
    try:
        # pdftotext -layout <pdf_path> -
        # -layout maintains physical layout which is often better for slides
        result = subprocess.run(['pdftotext', '-layout', pdf_path, '-'], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error processing PDF {pdf_path}: {e}")
        return None

def extract_text_from_pptx(pptx_path):
    text_content = []
    try:
        with zipfile.ZipFile(pptx_path, 'r') as z:
            # Find slide files
            slides = [f for f in z.namelist() if f.startswith('ppt/slides/slide') and f.endswith('.xml')]
            # Sort slides by number to maintain order
            # The filenames are like ppt/slides/slide1.xml, ppt/slides/slide2.xml
            try:
                slides.sort(key=lambda x: int(os.path.basename(x).replace('slide', '').replace('.xml', '')))
            except ValueError:
                # Fallback if naming is weird, just sort alphabetically
                slides.sort()

            for i, slide in enumerate(slides):
                xml_content = z.read(slide)
                root = ET.fromstring(xml_content)
                
                slide_text = []
                # Recursive search for text elements. 
                # Text is usually in {http://schemas.openxmlformats.org/drawingml/2006/main}t
                for elem in root.iter():
                    # We check endswith to handle namespaces loosely
                    if elem.tag.endswith('}t'):
                        if elem.text:
                            slide_text.append(elem.text)
                
                if slide_text:
                    text_content.append(f"## Slide {i + 1}")
                    text_content.append(" ".join(slide_text))
                    text_content.append("") # Empty line for spacing
                    
        return "\n".join(text_content)
    except Exception as e:
        print(f"Error processing PPTX {pptx_path}: {e}")
        return None

def main():
    root_dir = "."
    print("Starting slide conversion...")
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip .git and .obsidian directories
        if '/.git' in dirpath or '/.obsidian' in dirpath:
            continue

        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            base_name, ext = os.path.splitext(filename)
            ext = ext.lower()
            
            if ext not in ['.pdf', '.pptx']:
                continue

            mds_dir = os.path.join(dirpath, 'mds')
            if not os.path.exists(mds_dir):
                os.makedirs(mds_dir)

            output_path = os.path.join(mds_dir, base_name + ".md")
            
            # Skip if output already exists
            if os.path.exists(output_path):
                continue

            content = None
            if ext == '.pdf':
                print(f"Processing PDF: {file_path}")
                content = extract_text_from_pdf(file_path)
            elif ext == '.pptx':
                print(f"Processing PPTX: {file_path}")
                content = extract_text_from_pptx(file_path)
            
            if content:
                try:
                    with open(output_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Created: {output_path}")
                except Exception as e:
                    print(f"Failed to write {output_path}: {e}")

    print("Conversion complete.")

if __name__ == "__main__":
    main()
