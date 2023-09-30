# engiin hewleh uildel "\n" -> araas bichsen ug n shine mornoos ehlene
print("hello world")

# utgaa suuld bichih. ----> {} temdegiin orond format dotorh utguud orj irne.
print("{} vs {}".format("Python", "C#"))
print("My name is {}".format("Saikhnaa"))

# zai duurgej hewlene. ugee hed urttai hewleh we geh uyd ashiglana.
# jishee n husnegt bailaa gej bodohod bat dulamsuren 2 adilhan mornii zaind togsoh geh met uyd ashiglana.
print("{:>10}".format("python"))
print("{:>10}".format("p"))
print("My name is {:>10}".format("Saikhnaa"))

# ene tohioldol bol hoinoo zai awna.
print("My favorite programming language is {:15} :)".format("javascript"))

# tasdaj hewleh tuhai
# ur dund n ehnii 5n usgiig l hewlene
print("{:.5}".format("asdfghjklzxcvbnm"))

# too hewleh
# -> d = Decimal <- bol buhel too l hewlene. -> f = Float <- bol butarhai too
print("{:d}".format(25))
print("{:f}".format(25.2))
# deerh uildluud toon deer ch ajilna
print("{:6d}".format(25))
print("{:04.1f}".format(25.2))

# garaas utga awah
# jishee bolgoj deerh zuilsee ashiglaad ym hiij hariulay. dund n huwisagch ashiglana!
owog = input("Owog: ")
ner = input("Ner: ")
print("{:.1}.{}".format(owog, ner))

# split hiih ene n string -ig array bolgon huwirgadag ym.
# ene oilgoltuudig tsaashaa gun sudlana ghde anhan shatandaa ashigtai ashiglaj bolno.
# split hooson ashiglahad default utga n " " buyu hooson zaigaar salga bdag huswel oorchlon ywuulj bolno.
a, b, c = input().split() # 1 2 3
print(a, b, c) # 1 2 3
a, b, c = input().split("_") # 1_2_3
print(a, b, c) # 1 2 3

# ehnii eeljind uzej bgaa "fsdf" dotorh ug useg too-n string buyu oguulbert l ashigladag torol ym tiimes math uildel hiij chadahgu gsen ug.
# math uildel hiihin tuld tusgai torol bdag.

# Map ashiglan string torloo too ruu shiljuulj math uildel hiij bolno.
# Ghde map ashiglahgu ch too bolgoj bolno.
# Map shiglaj bga shaltgaan n 1 uildleer buh utgaa huwirgahad l ashiglaj bgan
# mon 2 oor toriin zuiliig nemj hasaj chadahgu. bid usegnees useg hasaj toonoos useg hasaj chadahgu shude!
n, m = map(int, input().split())
print("Sum: {}\n Mult: {}".format(n + m, n * m))

# Print ba Input inged ehnii eeljind duuslaa oorsdoo setgeed ym hiij uzeerei :)
