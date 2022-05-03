# Program name: Clement_Austin_FP
# Author: Austin Clement
# Date: 05/01/2022
# Summary: Program that provides a GUI that asks user for integer input, and an output that will convert the measurment to another measurment specified by the user through the buttons provided by the GUI.
# Variables:
#    

#import breezypythongui
from breezypythongui import EasyFrame

#delcare the class and initiliaze the main window
class MeasuringGUI(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Convert Measurements")


#create instruction label and text field in first row
        self.inputLabel = self.addLabel(text = "Enter a Measurement:", row = 0, column=0, sticky='w')
        self.inputField = self.addTextField(text='', row=0, column=1)
#create theoutput lable and output text field in second row
        self.outputLabel = self.addLabel(text= "Converted Measurement:", row=1, column=0)
        self.outputField = self.addTextField(text="", row=1, column=1, state="readonly")
#create the buttons in the third row
        self.CupstoFlOz_button = self.addButton(text= "Cups to Fl Oz", row=2, column=0, command= self.convert_CupstoFlOz)
        self.FlOztoCups_button = self.addButton(text= "Fl Oz to Cups", row=2, column=1, command= self.convert_FlOztoCups)
#create the buttons in the fourth row
        self.FlOztoTbsp_button = self.addButton(text= "Fl Oz to Tbsp", row=3, column=0, command= self.convert_FlOztoTbsp)
        self.TbsptoFlOz_button = self.addButton(text= "Tbsp to Fl Oz", row=3, column=1, command= self.convert_TbsptoFlOz)
#create the buttons in the fifth row
        self.TbsptoTsp_button = self.addButton(text= "Tbsp to Tsp", row=4, column=0, command= self.convert_TbsptoTsp)
        self.TsptoTbsp_button = self.addButton(text= "Tsp to Tbsp", row=4, column=1, command= self.convert_TsptoTbsp)    
#create the buttons in the sixth row
        self.TsptoMl_button = self.addButton(text= "Tsp to Ml", row=5, column=0, command= self.convert_TsptoMl)
        self.MltoTsp_button = self.addButton(text= "Ml to Tsp", row=5, column=1, command= self.convert_MltoTsp)
#define functions for third row
    def convert_CtoF(self):
        self.celsius = float(self.inputField.getText())
        self.fahrenheit = (9/5 * self.celsius) + 32
        self.outputField.setText(format(self.fahrenheit, '.2f'))

    def convert_FtoC(self):
        self.fahrenheit = float(self.inputField.getText())
        self.celsius = (self.fahrenheit - 32) * 5/9
        self.outputField.setText(format(self.celsius, '.2f'))
#define functions for fourth row
    def convert_CtoF(self):
        self.celsius = float(self.inputField.getText())
        self.fahrenheit = (9/5 * self.celsius) + 32
        self.outputField.setText(format(self.fahrenheit, '.2f'))

    def convert_FtoC(self):
        self.fahrenheit = float(self.inputField.getText())
        self.celsius = (self.fahrenheit - 32) * 5/9
        self.outputField.setText(format(self.celsius, '.2f'))
#define functions for fifth row
    def convert_CtoF(self):
        self.celsius = float(self.inputField.getText())
        self.fahrenheit = (9/5 * self.celsius) + 32
        self.outputField.setText(format(self.fahrenheit, '.2f'))

    def convert_FtoC(self):
        self.fahrenheit = float(self.inputField.getText())
        self.celsius = (self.fahrenheit - 32) * 5/9
        self.outputField.setText(format(self.celsius, '.2f'))
#define functions for sixth row
    def convert_CtoF(self):
        self.celsius = float(self.inputField.getText())
        self.fahrenheit = (9/5 * self.celsius) + 32
        self.outputField.setText(format(self.fahrenheit, '.2f'))

    def convert_FtoC(self):
        self.fahrenheit = float(self.inputField.getText())
        self.celsius = (self.fahrenheit - 32) * 5/9
        self.outputField.setText(format(self.celsius, '.2f'))
#start the main loop
def main():
    MeasuringGUI().mainloop()

main()