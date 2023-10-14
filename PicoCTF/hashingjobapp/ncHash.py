import hashlib

print("Enter the UTF-8 string:")
text = str(input(""))

md5_hash = hashlib.md5()
md5_hash.update(text.encode("utf-8"))
md5_hex = md5_hash.hexdigest()
print(md5_hex)