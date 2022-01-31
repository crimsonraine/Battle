from tkinter import *

class Screen_PrepareToBattle (Frame):
    def __init__ (self, master, player1, player2, callback_on_commence_battle):
        super().__init__(master)

        # Save player character object references
        self.player1 = player1
        self.player2 = player2
        
        # Save the method reference to which we return control after the player hits "Next"
        self.callback_on_commence_battle = callback_on_commence_battle
        
        self.create_widgets()
        self.grid()
        
    
    def create_widgets (self):
        self.player_lbl = Label(self, text = "You", font=("Times New Roman", 14))
        self.player_lbl.grid(row = 0, column = 0, sticky = W + E)
        
        self.computer_lbl = Label(self, text = "Computer", font=("Times New Roman", 14), fg = 'red')
        self.computer_lbl.grid(row = 0, column = 1, sticky = W + E)


        player_img = PhotoImage(file="images/" + self.player1.large_image)
        p1 = Label(self, image = player_img)
        p1.photo = player_img
        p1.grid(row = 1, column = 0, sticky = N)

        computer_img = PhotoImage(file="images/" + self.player2.large_image)
        p2 = Label(self, image = computer_img)
        p2.photo = computer_img
        p2.grid(row = 1, column = 1, sticky = N)

        self.player_hp_lbl = Label(self, text = f"{self.player1.hit_points} HP")
        self.player_hp_lbl.grid(row = 2, column = 0, sticky = N)

        self.player_dexterity_lbl = Label(self, text = f"{self.player1.dexterity} Dexterity")
        self.player_dexterity_lbl.grid(row = 3, column = 0, sticky = N)

        self.player_strength_lbl = Label(self, text = f"{self.player1.strength} Strength")
        self.player_strength_lbl.grid(row = 4, column = 0, sticky = N)


        self.computer_hp_lbl = Label(self, text = f"{self.player2.hit_points} HP")
        self.computer_hp_lbl.grid(row = 2, column = 1, sticky = N)

        self.computer_dexterity_lbl = Label(self, text = f"{self.player2.dexterity} Dexterity")
        self.computer_dexterity_lbl.grid(row = 3, column = 1, sticky = N)

        self.computer_strength_lbl = Label(self, text = f"{self.player2.strength} Strength")
        self.computer_strength_lbl.grid(row = 4, column = 1, sticky = N)

        self.commence_bttn = Button(self, text = "Commence Battle!", bg = 'black', fg = 'red')
        self.commence_bttn["command"] = self.commence_battle_clicked

        self.commence_bttn.grid(row = 5, column = 0, columnspan=2, pady = 5, sticky = S)
 
    def commence_battle_clicked(self):
        ''' This method is called when the Battle button is clicked. 
            It passes control back to the callback method. '''         
        self.callback_on_commence_battle()
            
        