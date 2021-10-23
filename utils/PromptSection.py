class Section:
    indent = 0
    indentChar = ""
    text = []

    def __init__(self, indent = 0, indentChar = " ") -> None:
        self.text = [""]
        self.indent = indent
        self.indentChar = indentChar
        
    
    def setIntent(self, num):
        self.indent = num
        return self

    def setIndentChar(self, char):
        self.indentChar = char
        return self

    def addText(self, text):
        self.text.append(text)
        return self

    def _getIndent(self):
        return "".join(self.indentChar for i in range(self.indent))

    def build(self):
        return  f"\n{self._getIndent()}".join(self.text)

    def toString(self):
        return self.build()
    
    def addBlank(self):
        self.addText("")
        return self
