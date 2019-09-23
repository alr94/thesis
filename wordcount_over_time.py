import matplotlib.pyplot as plt

text_file = open("wordcount.txt", "r")
lines = text_file.readlines()
for val in lines: val.strip("\n")
x = [int(val) for val in lines]
text_file.close()

plt.plot(x)
plt.show()
