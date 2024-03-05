contents = ["today i have to "
            "learn",
            "i should write on thursday",
            "Finally, it is already Friday"]
filenames= ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file= open(f"../files/{filename}", 'w')
    file.write(content)
