# dictdata={ x:x**x    for x in range(1,6)}
# print(dictdata)


# text="dfkjsadlkfjalkjfdakljfdlkadfjourndclamqasderfdxefrftngtujhujujymkiu,olnpk"
# strincount={x:text.count(x)   for x in text}
# print(strincount)

# vov='aeiou'
# text="dfkjsadlkfjalkjfdakljfdlkadfjourndclamqasderfdxefrftngtujhujujymkiu,olnpk"
# strincount={x:text.count(x)   for x in text if x in vov}
# print(strincount)


# text="dfkjsadlkfjalkjfdakljfdlkadfjourndclamqasderfdxefrftngtujhujujymkiu,olnpk"
# strincount={x  for x in text }
# print(strincount)

# vov='aeiou'
# text="dfkjsadlkfjalkjfdakljfdlkadfjourndclamqasderfdxefrftngtujhujujymkiu,olnpk"
# strincount={x  for x in text if x in vov}
# print(strincount)
data=[23,34,34,234,12,23,23,221,233,43]
bytedata=  bytes(data)
bytedataarr=  bytearray(data)
print(bytedata)
print(bytedataarr)