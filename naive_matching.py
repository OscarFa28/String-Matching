class StringMatching():
    
    def __init__(self):
        self.shifts = []
    
    def naive_matching(self, text, pattern): # regresa todas las incidencias del patrón en el texto
        self.size_of_text = len(text)
        self.size_of_pattern = len(pattern)
        for i in range(self.size_of_text - self.size_of_pattern + 1):
            temp = i
            for k in range(self.size_of_pattern):
                if pattern[k] != text[temp]:
                    break
                elif k == (self.size_of_pattern - 1):
                    self.shifts.append(i)
                temp += 1
                
        return self.shifts

text = "este es un texto de prueba que prueba textos"
pattern = "text"

st = StringMatching()

shifts = st.naive_matching(text, pattern) 

print(shifts)
print("Número de apariciones: "+str(len(shifts)))

            