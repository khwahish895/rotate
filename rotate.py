import pikepdf

old_pdf = pikepdf.Pdf.open("np.pdf.pdf ")
for i in old_pdf.pages:
    i.Rotate =180
    old_pdf.save("new_pdf.pdf")
