from docx import Document
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from copy import deepcopy

doc = Document('Prototype.docx')

def create_page_field():
    """Create a PAGE field (dynamic page number) as XML elements"""
    r1 = OxmlElement('w:r')
    fld_begin = OxmlElement('w:fldChar')
    fld_begin.set(qn('w:fldCharType'), 'begin')
    r1.append(fld_begin)
    
    r2 = OxmlElement('w:r')
    instr = OxmlElement('w:instrText')
    instr.set(qn('xml:space'), 'preserve')
    instr.text = ' PAGE '
    r2.append(instr)
    
    r3 = OxmlElement('w:r')
    fld_sep = OxmlElement('w:fldChar')
    fld_sep.set(qn('w:fldCharType'), 'separate')
    r3.append(fld_sep)
    
    r4 = OxmlElement('w:r')
    t = OxmlElement('w:t')
    t.text = '1'
    r4.append(t)
    
    r5 = OxmlElement('w:r')
    fld_end = OxmlElement('w:fldChar')
    fld_end.set(qn('w:fldCharType'), 'end')
    r5.append(fld_end)
    
    return [r1, r2, r3, r4, r5]

def clear_footer_paragraphs(footer):
    for p in footer._element.findall(qn('w:p')):
        footer._element.remove(p)

def set_footer_with_page_field(section, font_name='Times New Roman', font_size=12):
    footer = section.footer
    footer.is_linked_to_previous = False
    clear_footer_paragraphs(footer)
    
    p = OxmlElement('w:p')
    pPr = OxmlElement('w:pPr')
    jc = OxmlElement('w:jc')
    jc.set(qn('w:val'), 'center')
    pPr.append(jc)
    
    rPr = OxmlElement('w:rPr')
    rFonts = OxmlElement('w:rFonts')
    rFonts.set(qn('w:ascii'), font_name)
    rFonts.set(qn('w:hAnsi'), font_name)
    rPr.append(rFonts)
    sz = OxmlElement('w:sz')
    sz.set(qn('w:val'), str(font_size * 2))
    rPr.append(sz)
    szCs = OxmlElement('w:szCs')
    szCs.set(qn('w:val'), str(font_size * 2))
    rPr.append(szCs)
    
    elements = create_page_field()
    elements[0].insert(0, deepcopy(rPr))
    
    p.append(pPr)
    for el in elements:
        p.append(el)
    
    footer._element.append(p)

def set_pgnumtype(section, fmt='decimal', start='1'):
    sect_pr = section._sectPr
    existing = sect_pr.find(qn('w:pgNumType'))
    if existing is not None:
        sect_pr.remove(existing)
    pgNumType = OxmlElement('w:pgNumType')
    pgNumType.set(qn('w:fmt'), fmt)
    pgNumType.set(qn('w:start'), start)
    sect_pr.append(pgNumType)

sections = doc.sections
print(f"Total sections: {len(sections)}")

# Section 0 (Sampul): Roman, start=1
print("Section 0 (Sampul) -> Roman start=1")
set_pgnumtype(sections[0], fmt='lowerRoman', start='1')
set_footer_with_page_field(sections[0])

# Section 1 (Bagian Awal): linked
print("Section 1 (Bagian Awal) -> linked")
sections[1].footer.is_linked_to_previous = True

# Section 2 (BAB I): Arabic start=1
print("Section 2 (BAB I) -> Arabic start=1")
set_pgnumtype(sections[2], fmt='decimal', start='1')
set_footer_with_page_field(sections[2])

# Section 3 (BAB II): linked
print("Section 3 (BAB II) -> linked")
sections[3].footer.is_linked_to_previous = True

# Section 4 (BAB II cont): linked
print("Section 4 (BAB II cont) -> linked")
sections[4].footer.is_linked_to_previous = True

# Section 5 (BAB III): PAGE field (replace static "ii")
print("Section 5 (BAB III) -> PAGE field")
set_footer_with_page_field(sections[5])

# Section 6 (BAB IV): linked
print("Section 6 (BAB IV) -> linked")
sections[6].footer.is_linked_to_previous = True

# Section 7 (BAB V+): linked
print("Section 7 (BAB V+) -> linked")
sections[7].footer.is_linked_to_previous = True

doc.save('Prototype.docx')
print("\nDone! All footers fixed.")
