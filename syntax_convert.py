import lexer

token_exprs = [
    (r'[ \t]+',                 None),
    (r'#[^\n]*',                None),
    (r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',  None),
    (r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',  None),

    # Operasi Relasi
    (r'<=',                     "LEQ"),
    (r'<',                      "L"),
    (r'>=',                     "GEQ"),
    (r'>',                      "G"),
    (r'!=',                     "NEQ"),
    (r'\==',                    "ISEQ"),
    (r'\=(?!\=)',               "EQ"),

    # Integer and String
    (r'[\+\-]?[0-9]*\.[0-9]+',  "INT"),
    (r'[\+\-]?[1-9][0-9]+',     "INT"),
    (r'[\+\-]?[0-9]',           "INT"),
    (r'\"[^\"\n]*\"',           "STRING"),
    (r'\'[^\'\n]*\'',           "STRING"),

    # Syntax
    (r'\n',                     "NEWLINE"),
    (r'\(',                     "KBKI"), # Kurung Biasa KIri
    (r'\)',                     "KBKA"),
    (r'\[',                     "KSKI"), # Kurung Siku KIri
    (r'\]',                     "KSKA"),
    (r'\{',                     "KKKI"), # Kurung Kurawal Kiri
    (r'\}',                     "KKKA"),
    (r'\;',                     "TITIKKOMA"), 
    (r'\:',                     "TITIKDUA"),

    #Operasi Aritmatika
    (r'\*=',                    "MULAS"),
    (r'/=',                     "DIVAS"),
    (r'\+=',                    "SUMAS"),
    (r'-=',                     "SUBAS"),
    (r'\->',                    "ARROW"),
    (r'\+',                     "ADD"),
    (r'\-',                     "SUB"),
    (r'\*',                     "MUL"),
    (r'/',                      "DIV"),

    # Relational dalam syntax kata
    (r'\bformat\b',             "FORMAT"),
    (r'\band\b',                "AND"),
    (r'\bor\b',                 "OR"),
    (r'\bnot\b',                "NOT"),
    (r'\bif\b',                 "IF"),
    (r'\bthen\b',               "THEN"),
    (r'\belse\b',               "ELSE"),
    (r'\belif\b',               "ELIF"),

    # Looping
    (r'\bfor\b',                "FOR"),
    (r'\bwhile\b',              "WHILE"),
    (r'\brange\b',              "RANGE"),
    (r'\bbreak\b',              "BREAK"),
    (r'\bcontinue\b',           "CONTINUE"),
    (r'\bpass\b',               "PASS"),

    # Boolean
    (r'\bFalse\b',              "FALSE"),
    (r'\bTrue\b',               "TRUE"),
    (r'\bNone\b',               "NONE"),
    (r'\bin\b',                 "IN"),
    (r'\bis\b',                 "IS"),

    # Class dan Function
    (r'\bclass\b',              "CLASS"),
    (r'\bdef\b',                "DEF"),
    (r'\breturn\b',             "RETURN"),

    # Import
    (r'\bfrom\b',               "FROM"),
    (r'\bimport\b',             "IMPORT"),
    (r'\braise\b',              "RAISE"),
    (r'\bwith\b',               "WITH"),
    (r'\bas\b',                 "AS"),

    # Tipe Variabel
    (r'\bdict\b',               "TYPE"),
    (r'\bint\b',                "TYPE"),
    (r'\bstr\b',                "TYPE"),
    (r'\bfloat\b',              "TYPE"),
    (r'\bcomplex\b',            "TYPE"),
    (r'\blist\b',               "TYPE"),
    (r'\btuple\b',              "TIPE"),

    # Tambahan
    (r'\,',                     "COMMA"),
    (r'\w+[.]\w+',              "KARTITIK"),
    (r'\.',                     "TITIK"),
    (r'\[',                     "LSB"),
    (r'\]',                     "RSB"),
    (r'\{',                     "LCB"),
    (r'\}',                     "RCB"),
    (r'\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',       "MULTILINE"),
    (r'\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',       "MULTILINE"),
    (r'[A-Za-z_][A-Za-z0-9_]*', "ID"),
]

# def imp_lex(characters):
#     return lexer.lex(characters, token_exprs)