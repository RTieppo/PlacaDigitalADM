import zlib

def crc32(fileName):
    with open(fileName, 'rb') as fh:
        hash = 0
        while True:
            s = fh.read(65536)
            if not s:
                break
            hash = zlib.crc32(s, hash)
        return "%08X" % (hash & 0xFFFFFFFF)


eu = crc32('NASA2.png')
print(eu)




import urllib.request

f = open('NASA2.png','wb')
f.write(urllib.request.urlopen('https://images2.imgbox.com/e9/94/kgkGn9E6_o.png').read())
f.close()
print("download successful")