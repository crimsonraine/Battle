import tkinter as tk

class Screen_CharacterSelection (tk.Frame):
    def __init__ (self, master, roster, callback_on_selected):
        super().__init__(master)
       # Save the CharacterRoster  
        self.roster = roster
        # Save the method reference to which we return control after the player hits "Character Selected"
        self.callback_on_selected = callback_on_selected

        self.grid()
        self.create_widgets()
        
    def create_widgets (self):
        '''
        This method creates all of the widgets character selector page.
        The information about each character should be derived from self.roster, 
        which is a CharacterRoster loaded from battle_characters.txt. 
        The layout should NOT be hard-coded: if you re-order, alter, or remove entries 
        in battle_characters.txt, the layout should automatically reflect those changes. 
        
        ########
        
        The radio buttons on this page should all use the variable "self.character_index_index".  
        The values of the radio buttons must be a number equally the position of the character in the list. 
        For example, if the characters listed are Troll, Elf, Human, and Dwarf.  self.character_index would equal 0 
        for the Troll, 1 for the Elf, and so forth.  
        
        The variable self.character_index has been instantiated for your convenience below.
        
        ########

        Here is some sample code for including an image on a page:   (char is a Character object)
            
            imageSmall = tk.PhotoImage(file="images/" + char.small_image);
            w= tk.Label (self,
                        image = imageSmall, 
                         )
            w.photo = imageSmall # saving the image as a property is required for "saving" the image. It's odd.

            w.grid (ADD PARAMETERS HERE)
        '''

        self.character_index = tk.StringVar() # already put in
        self.character_index.set(None) # already put in

        # labels
        tk.Label(self, text="Hit Points", font=("Times New Roman", 12)).grid(row=0,column=3,sticky=tk.N, padx=(5,5))
        tk.Label(self, text="Dexterity", font=("Times New Roman", 12)).grid(row=0,column=4,sticky=tk.N, padx=(5,5))
        tk.Label(self, text="Strength", font=("Times New Roman", 12)).grid(row=0,column=5,sticky=tk.N, padx=(5,5))
        
        for c_i in range(len(self.roster.character_list)):# by indexes
            char = self.roster.character_list[c_i]
            tk.Radiobutton(self,
                #text = char.name,
                variable = self.character_index,
                value = c_i,
                ).grid(row = c_i + 1, column = 0, sticky = tk.W) # set position

            # name
            tk.Label(self, text=char.name, font=("Times New Roman", 12)).grid(row=c_i + 1,column=1,sticky=tk.N + tk.S, padx=(5,5))
            
            # image
            imageSmall = tk.PhotoImage(file="images/" + char.small_image);
            w= tk.Label (self, image = imageSmall)
            w.photo = imageSmall
            w.grid(row = c_i + 1, column = 2, sticky = tk.N)
            
            # stats
            tk.Label(self, text=char.hit_points, font=("Times New Roman", 12)).grid(row=c_i + 1,column=3,sticky=tk.N + tk.S, padx=(5,5))
            tk.Label(self, text=char.dexterity, font=("Times New Roman", 12)).grid(row=c_i + 1,column=4,sticky=tk.N + tk.S, padx=(5,5))
            tk.Label(self, text=char.strength, font=("Times New Roman", 12)).grid(row=c_i + 1,column=5,sticky=tk.N + tk.S, padx=(5,5))

        # character selected button
        self.char_select_button = tk.Button(self, text = "Character Selected!", bg = 'black', fg = 'red')
        self.char_select_button["command"] = self.selected_clicked

        self.char_select_button.grid(row=len(self.roster.character_list) + 1, column = 4, columnspan = 2, sticky = tk.E) 
        

       

    def selected_clicked(self):
        ''' This method is to be called when the "Character Selected!" button is clicked. 
            Notice that it passes self.character_index back to the callback method. '''         
        self.callback_on_selected(self.character_index.get())