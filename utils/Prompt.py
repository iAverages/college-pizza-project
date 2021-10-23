from utils.PromptSection import Section


class Prompt: 

    def __init__(self) -> None:
        self.sections = []

    def addText(self, text, indent = 0):
        self.addSection(Section(indent).addText(text))

    def addSection(self, section):
        if not isinstance(section, Section):
            raise "Only a section can be used."
        self.sections.append(section)
        
    def build(self):
        return "".join(self.sections[i].build() for i in range(len(self.sections)))

    def addBlank(self, num = 1):
        [self.addText("") for i in range(num)]
        return self
