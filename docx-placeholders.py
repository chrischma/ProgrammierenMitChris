from docx import Document


template_path = './templates/einladung.docx'
placeholder = "[[Name]]"
names = ['Arnold', 'Marie', 'Hans', 'Peter', 'Klaus', 'Karl', 'Lena', 'Lara', 'Lena']

for name in names: 
    document = Document(template_path)
    for p in document.paragraphs:
        if placeholder in p.text:
            p.text = p.text.replace(placeholder, name)
            
    document.save(f'einladung_von_{name}.docx')
        
