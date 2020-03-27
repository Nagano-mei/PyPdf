import PyPDF2

# with open("MIT6_lec05.pdf", "rb") as file:
#     reader = PyPDF2.PdfFileReader(file)
#     print(reader.numPages)
#     page = reader.getPage(0)
#     page.rotateClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open("rotated.pdf", "wb") as output:
#         writer.write(output)


merger = PyPDF2.PdfFileMerger()
file_names = ["MIT6_lec05.pdf","MIT6_lec06.pdf"]
for file_name in file_names:
    merger.append(file_name)
merger.write("combined.pdf")
