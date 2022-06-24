from tkinter import * # knihovna která umožňuje v Pythonu vytvářet např. okna
from tkinter import ttk
from tkinter import messagebox
import psycopg2



class Klient():
    # třída reprezentuje databázi klientů pojišťovny
    def __init__(self, root):
        self.root = root
        self.root.title("Databáze klientů pojišťovny")
        self.root.geometry("1370x700+0+0")
# vykreslení okna + nadpis
        title = Label(self.root, text = "Databáze klientů", bd = 9, relief = FLAT, font = ("times new roman", 40, "bold"), bg = "navy", fg = "gray97")
        title.pack(side = TOP, fill = X )

# proměnné =================================================================================================================================================================


        self.id_smlouvy_var = StringVar()
        self.jmeno_var = StringVar()
        self.email_var = StringVar()
        self.kontakt_var = StringVar()
        self.pojisteni_var = StringVar()
        self.nar_var = StringVar()
        self.vyhledavani_var = StringVar()
        self.vyhledavani_txt_var = StringVar()
        


# Správa klientů - jednotlivá okénka ===============================================================================================================================================================

        # umístění správy
        Manage_Okno = Frame(self.root, bd = 4, relief = FLAT, bg = "light slate gray")
        Manage_Okno.place(x = 20, y = 100, width = 450, height = 585)
        # nadpis správy
        s_title = Label(Manage_Okno, text = "Správa Klientů", bg = "light slate gray", fg = "gray5", font = ("times new roman", 25, "bold"))
        s_title.grid(row = 0, columnspan = 2, pady = 20)

        # konfigurace písma a okénka 1. řádek
        lbl_id_smlouvy = Label(Manage_Okno, text = "Č. smlouvy", bg = "light slate gray", fg = "gray5", font = ("times new roman", 15, "bold"))
        lbl_id_smlouvy.grid(row = 1, column = 0, pady = 10, padx = 20, sticky = "w")
        txt_ID_smlouvy = Entry(Manage_Okno, textvariable = self.id_smlouvy_var, font = ("times new roman", 15, "bold"), bd = 5, relief = FLAT)
        txt_ID_smlouvy.grid(row = 1, column = 1, pady = 10, padx = 20, sticky = "w")

        # konfigurace písma a okénka 2. řádek
        lbl_jmeno = Label(Manage_Okno, text = "Jméno a Příjmení", bg = "light slate gray", fg = "gray5", font = ("times new roman", 15, "bold"))
        lbl_jmeno.grid(row = 2, column = 0, pady = 10, padx = 20, sticky = "w")
        txt_Jmeno = Entry(Manage_Okno, textvariable = self.jmeno_var, font = ("times new roman", 15, "bold"), bd = 5, relief = FLAT)
        txt_Jmeno.grid(row = 2, column = 1, pady = 10, padx = 20, sticky = "w")

        # konfigurace písma a okénka 3. řádek
        lbl_email = Label(Manage_Okno, text = "Email", bg = "light slate gray", fg = "gray5", font = ("times new roman", 15, "bold"))
        lbl_email.grid(row = 3, column = 0, pady = 10, padx = 20, sticky = "w")
        txt_Email = Entry(Manage_Okno, textvariable = self.email_var, font = ("times new roman", 15, "bold"), bd = 5, relief = FLAT)
        txt_Email.grid(row = 3, column = 1, pady = 10, padx = 20, sticky = "w")


        # konfigurace písma a okénka 4. řádek
        lbl_kontakt = Label(Manage_Okno, text = "Kontakt", bg = "light slate gray", fg = "gray5", font = ("times new roman", 15, "bold"))
        lbl_kontakt.grid(row = 5, column = 0, pady = 10, padx = 20, sticky = "w")
        txt_Kontakt = Entry(Manage_Okno, textvariable = self.kontakt_var, font = ("times new roman", 15, "bold"), bd = 5, relief = FLAT)
        txt_Kontakt.grid(row = 5, column = 1, pady = 10, padx = 20, sticky = "w")


        # konfigurace písma 5. řádek
        lbl_pojisteni = Label(Manage_Okno, text = "Pojištění", bg = "light slate gray", fg = "gray5", font = ("times new roman", 15, "bold"))
        lbl_pojisteni.grid(row = 6, column = 0, pady = 10, padx = 20, sticky = "w")

        # výběr - druh pojištění 5. řádek
        combo_Pojisteni = ttk.Combobox(Manage_Okno, textvariable = self.pojisteni_var, font = ("times new roman", 13, "bold"), state = 'readonly')
        combo_Pojisteni['values'] = ("Životní pojištění", "Pojištění domácnosti", "Úrazové pojištění", "Kombo")
        combo_Pojisteni.grid(row = 6, column = 1, pady = 10, padx = 20)


        # konfigurace písma a okénka 6. řádek
        lbl_nar = Label(Manage_Okno, text = "Datum narození", bg = "light slate gray", fg = "gray5", font = ("times new roman", 15, "bold"))
        lbl_nar.grid(row = 7, column = 0, pady = 10, padx = 20, sticky = "w")
        txt_Nar = Entry(Manage_Okno, textvariable = self.nar_var, font = ("times new roman", 15, "bold"), bd = 5, relief = FLAT)
        txt_Nar.grid(row = 7, column = 1, pady = 10, padx = 20, sticky = "w")

        # konfigurace písma a okénka 7. řádek
        lbl_adresa = Label(Manage_Okno, text = "Adresa", bg = "light slate gray", fg = "gray5", font = ("times new roman", 15, "bold"))
        lbl_adresa.grid(row = 8, column = 0, pady = 10, padx = 20, sticky = "w")
        self.txt_Adresa = Text(Manage_Okno, width = 29, height = 3, font = ("times new roman", 10, "bold"), bd = 5, relief = FLAT)
        self.txt_Adresa.grid(row = 8, column = 1, pady = 10, padx = 20, sticky = "w")


# tlačítka ===================================================================================================================================================================


        # umístění tlačítek
        btn_frame = Frame(Manage_Okno, bd = 3, relief = FLAT, bg = "light slate gray")
        btn_frame.place(x = 15, y = 525, width = 420)

        Add_btn = Button(btn_frame, text = "Add", width = 10, command = self.add_klient).grid(row = 0, column = 0, padx = 10, pady = 10)
        Update_btn = Button(btn_frame, text = "Update", width = 10, command = self.update_data).grid(row = 0, column = 1, padx = 10, pady = 10)
        Delete_btn = Button(btn_frame, text = "Delete", width = 10, command = self.delete_data).grid(row = 0, column = 2, padx = 10, pady = 10)
        Clear_btn = Button(btn_frame, text = "Clear", width = 10, command = self.clear).grid(row = 0, column = 3, padx = 10, pady = 10)
        

# vyhledávání klientů================================================================================================================================================================

        # umístění
        Klient_Okno = Frame(self.root, bd = 4, relief = FLAT, bg = "light slate gray")
        Klient_Okno.place(x = 500, y = 100, width = 880, height = 585)
        # nadpis roletky
        lbl_vyhledavani = Label(Klient_Okno, text = "Vyhledat podle:", bg = "light slate gray", fg = "gray5", font = ("times new roman", 20, "bold"))
        lbl_vyhledavani.grid(row = 0, column = 0, pady = 10, padx = 20, sticky = "w")
        # roletka s nabídkou
        combo_vyhledavani = ttk.Combobox(Klient_Okno, textvariable = self.vyhledavani_var, font = ("times new roman", 13), state = 'readonly')
        combo_vyhledavani['values'] = ("id_smlouvy", "jmeno_prijmeni", "email", "kontakt", "pojisteni", "datum_narozeni", "adresa")
        combo_vyhledavani.grid(row = 0, column = 1, pady = 10, padx = 20)
        # okénko zadávání
        txt_vyhledavani = Entry(Klient_Okno, textvariable = self.vyhledavani_txt_var, font = ("times new roman", 10, "bold"),width = 20, bd = 5, relief = FLAT)
        txt_vyhledavani.grid(row = 0, column = 2, pady = 10, padx = 20, sticky = "w")

# talčítka vyhledávání =====================================================================================================================================================================

        btn_vyhledavani = Button(Klient_Okno, text = "Hledat", width = 10, pady = 5, command = self.search_data).grid(row = 0, column = 3, padx = 10, pady = 10)
        showall_btn = Button(Klient_Okno, text = "Ukázat vše", width = 10, pady = 5, command = self.fetch_data).grid(row = 0, column = 4, padx = 10, pady = 10)


# okno seznamu (Tabule) ====================================================================================================================================================================

        # vykreslení okna
        Okno_Tabule = Frame(Klient_Okno, bd = 4, relief = FLAT, bg = "gray97")
        Okno_Tabule.place(x = 58, y = 65, width = 760, height = 500)
        
        # scrollování v okně
        scroll_x = Scrollbar(Okno_Tabule, orient = HORIZONTAL)
        scroll_y = Scrollbar(Okno_Tabule, orient = VERTICAL)

        # sloupce
        self.Klient_Tabule = ttk.Treeview(Okno_Tabule, column = ("ID smlouvy", "Jméno a příjmení", "Email", "Kontakt", "Pojištění", "Datum narození", "Adresa"), xscrollcommand = scroll_x, yscrollcommand = scroll_y)
        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)

        scroll_x.config()
        scroll_y.config()


        # položky v okně
        self.Klient_Tabule.heading("ID smlouvy", text = "ID smlouvy") 
        self.Klient_Tabule.heading("Jméno a příjmení", text = "Jméno a příjmení")
        self.Klient_Tabule.heading("Email", text = "Email")
        self.Klient_Tabule.heading("Kontakt", text = "Kontakt")
        self.Klient_Tabule.heading("Pojištění", text = "Pojištění")
        self.Klient_Tabule.heading("Datum narození", text = "Datum narození")
        self.Klient_Tabule.heading("Adresa", text = "Adresa")
 

        self.Klient_Tabule['show'] = 'headings'
        self.Klient_Tabule.column("ID smlouvy", width = 100) 
        self.Klient_Tabule.column("Jméno a příjmení", width = 100)
        self.Klient_Tabule.column("Email", width = 100)
        self.Klient_Tabule.column("Kontakt", width = 100)
        self.Klient_Tabule.column("Pojištění", width = 100)
        self.Klient_Tabule.column("Datum narození", width = 100)
        self.Klient_Tabule.column("Adresa", width = 150)


        self.Klient_Tabule.pack(fill = BOTH, expand = 1)
        self.Klient_Tabule.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()



    # metoda pro přidání klienta
    def add_klient(self):
        if self.id_smlouvy_var.get() == "" or self.id_smlouvy_var.get() == "":
                messagebox.showerror("Je nutné vyplnit všechna pole!") # info okénko 
        else:
                connection = psycopg2.connect(user="postgres",
                                        password="Knittel3556",
                                        host="localhost",
                                        port="5432",
                                        database="postgres")

                cursor = connection.cursor()
                cursor.execute("insert into test.klienti values (%s, %s, %s, %s, %s, %s, %s)", (self.id_smlouvy_var.get(),
                                                                                                self.jmeno_var.get(),
                                                                                                self.email_var.get(),
                                                                                                self.kontakt_var.get(),
                                                                                                self.pojisteni_var.get(),
                                                                                                self.nar_var.get(),
                                                                                                self.txt_Adresa.get('1.0', END)))
                connection.commit()
                self.fetch_data()
                self.clear()
                connection.close()
                messagebox.showinfo("Uloženo!") # info okénko 

    # metoda návratu dat z tabulky
    def fetch_data(self):
                connection = psycopg2.connect(user="postgres",
                                        password="Knittel3556",
                                        host="localhost",
                                        port="5432",
                                        database="postgres")

                cursor = connection.cursor()
                cursor.execute("select * from test.klienti")
                rows = cursor.fetchall()
                if len(rows) != 0:
                        self.Klient_Tabule.delete(*self.Klient_Tabule.get_children())
                        for row in rows:
                            self.Klient_Tabule.insert('', END, values = row)
                        connection.commit()
                connection.close()

    # metoda pro vypsání dat zpět do správy klientů
    def get_cursor(self, ev):
                cursor_row = self.Klient_Tabule.focus()
                contents = self.Klient_Tabule.item(cursor_row)

                row = contents['values']
                self.id_smlouvy_var.set(row[0])
                self.jmeno_var.set(row[1])
                self.email_var.set(row[2])
                self.kontakt_var.set(row[3])
                self.pojisteni_var.set(row[4])
                self.nar_var.set(row[5])
                self.txt_Adresa.delete("1.0", END)
                self.txt_Adresa.insert(END, row[6])

                 
    # metoda pro vyčištění oken správy klientů
    def clear(self):
        self.id_smlouvy_var.set("")
        self.jmeno_var.set("")
        self.email_var.set("")
        self.kontakt_var.set("")
        self.pojisteni_var.set("")
        self.nar_var.set("")
        self.txt_Adresa.delete("1.0", END)

    # metoda pro update dat
    def update_data(self):
        
                connection = psycopg2.connect(user="postgres",
                                        password="Knittel3556",
                                        host="localhost",
                                        port="5432",
                                        database="postgres")

                cursor = connection.cursor()
                cursor.execute("update test.klienti set jmeno_prijmeni = %s, email = %s, kontakt = %s, pojisteni = %s, datum_narozeni = %s, adresa = %s where id_smlouvy = %s", 
                                                                                               (self.jmeno_var.get(),
                                                                                                self.email_var.get(),
                                                                                                self.kontakt_var.get(),
                                                                                                self.pojisteni_var.get(),
                                                                                                self.nar_var.get(),
                                                                                                self.txt_Adresa.get('1.0', END),
                                                                                                self.id_smlouvy_var.get()))
                connection.commit()
                self.fetch_data()
                self.clear()
                connection.close()
                messagebox.showinfo("Uloženo!")

    # metoda pro smazání klienta
    def delete_data(self):
                connection = psycopg2.connect(user="postgres",
                                        password="Knittel3556",
                                        host="localhost",
                                        port="5432",
                                        database="postgres")

                cursor = connection.cursor()
                cursor.execute("delete from test.klienti where id_smlouvy = %s", self.id_smlouvy_var.get())
                connection.commit()
                connection.close()
                self.fetch_data()
                self.clear()

    # metoda pro hledání klienta
    def search_data(self):
                connection = psycopg2.connect(user="postgres",
                                        password="Knittel3556",
                                        host="localhost",
                                        port="5432",
                                        database="postgres")

                cursor = connection.cursor()
                cursor.execute("select * from test.klienti where "+str(self.vyhledavani_var.get())+"::text Like '%"+str(self.vyhledavani_txt_var.get())+"%';")
                rows = cursor.fetchall()
                if len(rows) != 0:
                        self.Klient_Tabule.delete(*self.Klient_Tabule.get_children())
                        for row in rows:
                            self.Klient_Tabule.insert('', END, values = row)
                        connection.commit()
                connection.close()




class Klient():
    root = Tk()
    obj = Klient(root)
    root.mainloop()

