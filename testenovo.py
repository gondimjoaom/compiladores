import sys
import string
import re

def is_number_letter(s):
        return all(((ord(c) > 31 and ord(c) < 127) or ord(c) == 10 or ord(c)== 9) for c in s)

class Token(object):
    #PARA QUANDO FOR FAZER A PARTE SINTATICA
    def __init__(self, type, valor, posicao, linha):
        self.type = False
        self.valor = valor
        self.posicao = posicao
        self.linha = linha
    def __str__(self):
        return None
class Erro(Exception):
    def __init__(self, posicao, linha):
        self.posicao = posicao
        self.linha = linha

class Analyzer(object):
    def __init__(self, regras):
        self.regras = []
        for expreg, type in regras:
            self.regras.append((re.compile(expreg),type))
    def entrada(self, buffer):
        self.buffer = buffer
        self.posicao = 0
        self.linha = 1
    def token(self):
        if self.posicao == len(self.buffer):
            print("dkslfj")
            self.linha += 1
        if self.posicao >= len(self.buffer):
            print("dkslfj")
            return None
        if True: #isso aqui faz pular os espacos em branco
            espaco_Branco = re.compile('\S') #NAO ENCONTRA ESPACO EM BRANCO
            m = espaco_Branco.search(self.buffer, self.posicao) #search retorna apenas se achar um match
            if m:
                self.posicao = m.start()
            else:
                return None
        for expreg, type in self.regras:
            m = expreg.match(self.buffer, self.posicao)
            if m:
                #para quand comecar o sintatico
                simbolo = Token(type, m.group(), self.posicao, self.linha) #group pega toda a match
                self.posicao = m.end()
                return simbolo
        raise Erro(self.posicao, self.linha)
    def it_token(self):
        while True:
            simbolo = self.token()
            if simbolo is None:
                break
            yield simbolo

if __name__ == "__main__":

    regras = [
        ('(^[a-zA-Z][_]*[_a-z_A-Z_0-9]*)|(^[_][_a-z_A-Z_0-9]+)', 'Identificador'),
        ('\d+\.*\d*', 'Numero'),
        ('\+', 'Soma')
    ]
    jump = False
    tudo_certo = True
    lx = Analyzer(regras)
    #input_str = sys.stdin.read()
    i = 0
    new_string = []
    #for string in sys.stdin:
    string = sys.stdin.read()
    #lx.input('a0+9a')
        #new_string.append(string)

    if not(is_number_letter(string)):
        jump = True
    if jump:
        print("ARQUIVO INVALIDO")
    else:
        #file = sys.stdin
        #print(new_string)
        lx.entrada(string)
        '''
        try:
            for tok in lx.it_token():
                continue
                #print("match")
        except Erro as err:
            tudo_certo = False
            h = int(err.posicao) + 1
            print(str(i) + " " + str(h))
            #print(str(i) + " " + '%s' % err.posicao)'''
        try:
            for tok in lx.it_token():
                continue
                #print("match")
        except Erro as err:
            tudo_certo = False
            h = int(err.posicao) + 1
            #print(str(i) + " " + str(h))
            print('%s' %err.linha)
            print(' ' + '%s' % err.posicao)            
        if tudo_certo:
            print ("OK")