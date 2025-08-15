class Solution(object):
    def reverseWords(self, s):
        #prvo otklonimo bilo koje prazno mijesto
        #na pocetku i na kraju stringa
        mystr= s.strip()
        #zatim napravimo listu rasclanjenjem stringa
        #napomena: da smo stavili s.split(' '), onda bi
        #otklonili samo jedan whitespace
        lst = mystr.split()
        #'prevrtanje' liste
        lst = lst[::-1]
        #funkcija vraca elemente liste spojene separatorom (razmakom)
        sep = ' '
        return sep.join(lst)
        