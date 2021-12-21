def contarPalabras(archivoPalabras):
    archivo = open(archivoPalabras, 'r')
    palabras = {}
    for linea in archivo:
        palabras[linea.strip()] = []

    print('Lista de palabras:\n', palabras)
    archivo.close()


def contarFrases(palabras, archivoFrases):
    archivo = open(archivoFrases, 'r')
    frases = {}
    for frase in archivo:
        frases.append(frase.strip())
        for palabra in palabras:
            palabras[palabra].append()(frase.lower().count(palabra))

    archivo.close()


class FindPal:
    def _init_(self, archivoPalabras, archivoFrases):
        self.archivoPalabras = archivoPalabras
        self.archivoFrases = archivoFrases

        self.palabras = contarPalabras(archivoPalabras)
        self.frases = contarFrases(self.palabras, archivoFrases)