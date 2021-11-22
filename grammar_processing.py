# ATURAN MENULIS GRAMMAR:
# Head pertama akan menjadi Start Symbol
# Variables ditulis huruf uppercase atau angka semua (untuk precaution juga jangan pake nama "START", "X", "Y", "Z"), sedangkan Terminal harus mengandung huruf lowercase
# Variables yang ditulis pada txt tidak boleh mengandung angka
# Tidak mengandung Useless Production (tidak terdapat Variables yang tidak dapat diderivasi menjadi string dan tidak terdapat Productions yang tidak muncul pada derivasi string)
# Tidak mengandung Null Production (tidak terdapat Variables yang menghasilkan epsilon, kecuali pada Start Symbol)

def read_grammar(nama_file):
    file = open(nama_file, "r")
    cfg = {}

    baris = file.readline()
    while baris != "":
        head, body = baris.replace("\n", "").split(" -> ")
        
        if head not in cfg.keys():
            cfg[head] = [body.split(" ")]
        else:
            cfg[head].append(body.split(" "))

        baris = file.readline()

    file.close()

    return cfg

def is_variables(string):
    return all([char.isupper() or char.isnumeric() for char in string])

def is_terminal(string):
    return any([char.islower() for char in string])