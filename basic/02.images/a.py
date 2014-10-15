
from kivy.uix.accordion import Accordion, AccordionItem


    def addPiano(self):
        self.apiano = AccordionItem(title='Carnatic Piano')
        self.piano = PianoBox()
        self.apiano.add_widget(self.piano)
        self.add_widget(self.apiano)
        self.apiano.bind(collapse=self.carnaticPianoIsActive)


from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelHeader
from kivy.uix.tabbedpanel import TabbedPanelItem

