# Help Cited: Parth Jain

import tkinter as tk

class Screen_Battle (tk.Frame):
    def __init__ (self, master, player1, player2, callback_on_exit):
        super().__init__(master)

        # Save references to the two player objects
        self.player1 = player1
        self.player2 = player2

        # Store the maximum number of hit points which are needed on the screen display.
        self.player1_max_hp = player1.hit_points
        self.player2_max_hp = player2.hit_points

        # Save the method reference to which we return control after this page Exits.
        self.callback_on_exit = callback_on_exit

        self.create_widgets()
        self.grid()
        
    def create_widgets (self):
        '''
        This method creates all of the (initial) widgets for the battle page.
        '''
        self.atk_bttn = tk.Button(self, text = "Attack!", bg = 'black', fg = 'red')
        self.atk_bttn["command"] = self.attack_clicked
        self.atk_bttn.grid(row = 0, column = 0, pady = 5, sticky = tk.N)

        # three lines of labels for move announcements
        self.annc_atk = tk.Label(self) 
        self.annc_atk.grid(row = 0, column = 2, sticky = tk.N) 
        self.annc_atk2 = tk.Label(self)
        self.annc_atk.grid(row = 1, column = 2, sticky = tk.N) 
        self.annc_atk3 = tk.Label(self) 
        self.annc_atk3.grid(row = 2, column = 2, sticky = tk.N) 

        self.player_lbl = tk.Label(self, text = "You", font=("Times New Roman", 14))
        self.player_lbl.grid(row = 3, column = 0, sticky = tk.W + tk.E)
        
        self.computer_lbl = tk.Label(self, text = "Computer", font=("Times New Roman", 14), fg = 'red')
        self.computer_lbl.grid(row = 3, column = 1, sticky = tk.W + tk.E)


        player_img = tk.PhotoImage(file="images/" + self.player1.large_image)
        p1 = tk.Label(self, image = player_img)
        p1.photo = player_img
        p1.grid(row = 4, column = 0, sticky = tk.N)

        computer_img = tk.PhotoImage(file="images/" + self.player2.large_image)
        p2 = tk.Label(self, image = computer_img)
        p2.photo = computer_img
        p2.grid(row = 4, column = 1, sticky = tk.N)

        self.init_player_hp = self.player1.hit_points
        self.init_computer_hp = self.player2.hit_points

        # finish adjusting hp labels to match example
        self.player_hp_lbl = tk.Label(self, text = f"{self.player1.hit_points}/{self.init_player_hp} HP")
        self.player_hp_lbl.grid(row = 5, column = 0, sticky = tk.N)

        self.computer_hp_lbl = tk.Label(self, text = f"{self.player2.hit_points}/{self.init_computer_hp} HP")
        self.computer_hp_lbl.grid(row = 5, column = 1, sticky = tk.N)

        self.commence_bttn = tk.Button(self, text = "Exit", bg = 'black', fg = 'red')
        self.commence_bttn["command"] = self.exit_clicked

        
        
    def attack_clicked(self):
        self.annc_atk['text'] = self.player1.attack(self.player2)
        
        if self.player2.hit_points > 0:
            self.annc_atk2['text'] = self.player2.attack(self.player1)

        if self.player1.hit_points <= 0: 
            self.annc_atk3(self, text = self.player2.name + "wins")
            self.atk_bttn.destroy() 
            self.exit_btn = tk.Button(self, text = "Exit", bg = 'black', fg = 'red')
            self.exit_btn["command"] = self.exit_clicked()
            self.exit_btn.grid(row = 0, column = 0, pady = 5, sticky = tk.N)

        elif self.player2.hit_points <= 0: 
            self.annc_atk3(self, text = self.player1.name + "wins")
            self.atk_bttn.destroy() 
            self.exit_btn = tk.Button(self, text = "Exit", bg = 'black', fg = 'red')
            self.exit_btn["command"] = self.exit_clicked()
            self.exit_btn.grid(row = 0, column = 0, pady = 5, sticky = tk.N)

        self.player_hp_lbl = tk.Label(self)
        self.player_hp_lbl["text"] = f"{self.player1.hit_points}/{self.player1_max_hp} HP"
        self.player_hp_lbl.grid(row = 3, column = 0, sticky = tk.N)

        self.computer_hp_lbl = tk.Label(self)
        self.computer_hp_lbl["text"] = f"{self.player2.hit_points}/{self.player2_max_hp} HP"
        self.computer_hp_lbl.grid(row = 3, column = 1, sticky = tk.N)

                                            
    def exit_clicked(self):
        ''' This method is called when the Exit button is clicked. 
            It passes control back to the callback method. '''        
        self.callback_on_exit()