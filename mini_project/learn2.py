class Number:
    def __init__(self, num, letter):
        self.numb = num
        self.alphabEt = letter

    def calc(say, adD):
        say.tem = adD
        print('testing is easy ' + say.alphabEt)
        print('testing is easy ' + str(say.tem))

ks = Number(54, 'worder')
print(ks.alphabEt)
print(ks.numb)
ks.calc(10)


class Number15(Number):
    def __init__(self, nuM, WORD, alphnumB):
        super().__init__(nuM, WORD)
        self.alphnumB = alphnumB

    def final(self):
        print(f'I have understood this {self.numb}, {self.alphabEt} and {self.alphnumB}') 

    def addmore(self, onemore):
        print(f'I added {onemore} to the existing {self.numb}, {self.alphabEt} and {self.alphnumB}')

y = Number15(60, 'Akin', 'asgdgdj4848')
y.final()
y.addmore(6)
