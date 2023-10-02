# ehleed help.txt dotorhiig unshaad uzeerei. pls read to help.txt
# toon huwisagch. int buyu buhel too float buyu butarhai too complex too gsen torluudtei
a = 5
b = 5.5
c = -10
ac = 21345678976543567
# ymar 1n huwisagchiin ogogdliin torliig harahdaa. type() ashiglana
myType = type(323.22)
print("type is: ", myType)
# 1e6 gwel 0 nemdeg jishee n ened 1in ard 6n 0 gsen ug. 1000000
# harin 1e-4 gwel arawtruu 0.0001

# complex too
com = 2 + 1j
print(com + 2 + 3j) # 4 + 4j
# zarim 1 function
# abs(number) eyreg utga ruu ywuuldag
print(abs(-100))
# int(number) buhel hesgiig awna
print(int(2.23))
# float(number) toog butarhai too bolgono
print(float(2))
# complex(number) toog complex too bolgono
print(complex(2))
# hex(number) 16-in toollin system ruu horwuulne

# logic operator buyu boolean
# boolean utga n True False gsen 2 l utgatai
isMale = True
isFeMale = False
# harin zereg shalgah utguud bdag ba and operator n shalgaj bui nohtsoluud bugd unen bh shaardlagatai uyd ashiglana.
# busad hel deer && (isMale && isFeMale) gedeg bol python deer.
Male = isMale and isFeMale
print(Male, type(Male))
# bas or operator bdag ba shalgaj bui nohtsoluud ali 1n unen bh uyd ashiglana.
# busad hel deer && (isMale || isFeMale) gedeg bol python deer.
noGay = isMale or isFeMale
print(noGay)
# shalgadag utga bdag ba programmin hel deer utga onoohdoo a = 3 gdeg n a gdeg huwisagchid 3 gsen utgiig onooh buyu a-g ashiglah uyd ard n 3 gdeg utga bn gsen uy.
# harin a == 1 gdeg bol a gdeg huwisagch n 1 mon u gsen ug. mon uuntei adil < ,> , <= , >= bas bdag

# string
str = "hello world"
print(str, type(str))
# string torol n hoorondoo shuud nemegdej boldog
print(str + " in python")
# mon urjij boldog urjih uyd tuhain string urjsen udaa boldog
print(str * 3)
# zarin function
# upper() buh usgiig tom bolgono
print(str.upper())
# upper() buh usgiig jijig bolgono
print(str.lower())
# strip() zai bwal arilgadag urd hoinoos. replace() solidog.
print(str.replace("world", "Earth"))


