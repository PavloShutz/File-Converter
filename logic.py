import convertapi
convertapi.api_secret = 'inA90W4czyFbrojQ'

result = convertapi.convert('doxc', { 'File': r'C:\Users\Lenovo\Desktop\test.txt' })

print(result)
# save to file
result.file.save(r'F:\Python\File Converter\test.docx')
