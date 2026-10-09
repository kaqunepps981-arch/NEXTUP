import tkinter as tk
from tkinter import messagebox

BG = '#101010'
PANEL = '#191919'
RED = '#e32636'
WHITE = '#f4f4f4'
MUTED = '#b5b5b5'

class NextUpLauncher(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('NEXTUP')
        self.geometry('900x560')
        self.minsize(760, 480)
        self.configure(bg=BG)
        self.sidebar = tk.Frame(self, bg='#080808', width=190)
        self.sidebar.pack(side='left', fill='y')
        self.sidebar.pack_propagate(False)
        tk.Label(self.sidebar, text='NEXTUP', bg='#080808', fg=RED,
                 font=('Segoe UI', 25, 'bold')).pack(pady=(28, 4))
        tk.Label(self.sidebar, text='NBA 2K20 COMMUNITY', bg='#080808', fg=MUTED,
                 font=('Segoe UI', 8, 'bold')).pack(pady=(0, 28))
        self.content = tk.Frame(self, bg=BG)
        self.content.pack(side='left', fill='both', expand=True)
        for name in ('Home', 'Whitelist', 'Rewards', 'Settings'):
            tk.Button(self.sidebar, text=name, anchor='w', padx=22, pady=12,
                      bg='#080808', fg=WHITE, activebackground=RED,
                      activeforeground='white', relief='flat', bd=0,
                      font=('Segoe UI', 11), command=lambda n=name: self.show_page(n)
                      ).pack(fill='x', padx=10, pady=3)
        self.show_page('Home')

    def show_page(self, page):
        for child in self.content.winfo_children():
            child.destroy()
        tk.Label(self.content, text=page.upper(), bg=BG, fg=WHITE,
                 font=('Segoe UI', 23, 'bold')).pack(anchor='w', padx=34, pady=(30, 18))
        if page == 'Home':
            tk.Label(self.content, text='Your community hub starts here.', bg=BG, fg=WHITE,
                     font=('Segoe UI', 16)).pack(anchor='w', padx=34, pady=8)
            tk.Label(self.content, text='This is a starter interface. Online features need a compatible community backend.',
                     bg=BG, fg=MUTED, wraplength=620, justify='left',
                     font=('Segoe UI', 10)).pack(anchor='w', padx=34, pady=5)
            tk.Button(self.content, text='CHECK LOCAL BACKEND', bg=RED, fg='white',
                      activebackground='#b91d2a', relief='flat', padx=16, pady=10,
                      command=self.check_backend).pack(anchor='w', padx=34, pady=22)
        elif page == 'Whitelist':
            self.info('Discord role syncing is not connected yet. Mods, Content Creator, and Beta Tester are planned roles.')
        elif page == 'Rewards':
            self.info('Reward display is a placeholder. No player ratings or badges are being changed by this launcher yet.')
        else:
            self.info('Settings will hold your game path and connection preferences. Do not enter Steam passwords or bot tokens here.')

    def info(self, text):
        tk.Label(self.content, text=text, bg=PANEL, fg=WHITE, wraplength=600,
                 justify='left', padx=22, pady=20, font=('Segoe UI', 11)).pack(anchor='nw', padx=34, pady=4, fill='x')

    def check_backend(self):
        messagebox.showinfo('NEXTUP backend', 'This starter build does not connect to a backend yet. See backend/README.md for the local API prototype.')

if __name__ == '__main__':
    NextUpLauncher().mainloop()
