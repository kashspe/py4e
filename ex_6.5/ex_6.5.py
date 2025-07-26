text = "X-DSPAM-Confidence:    0.8475"
text_wos = text.replace(" ","")

dppos = text_wos.find(":")


number = text_wos[dppos+1:]
print(float(number))