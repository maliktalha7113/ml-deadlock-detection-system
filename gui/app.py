import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess


class DeadlockGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ML-Based Deadlock Detection & Recovery System")
        self.root.geometry("700x520")
        self.root.resizable(False, False)

        # ---------- STYLE ----------
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Header.TLabel",
            font=("Segoe UI", 18, "bold")
        )

        style.configure(
            "Status.TLabel",
            font=("Segoe UI", 11)
        )

        style.configure(
            "TButton",
            font=("Segoe UI", 11),
            padding=6
        )

        # ---------- HEADER ----------
        header = ttk.Label(
            root,
            text="Machine Learning–Based Deadlock Detection System",
            style="Header.TLabel"
        )
        header.pack(pady=15)

        # ---------- STATUS ----------
        self.status = ttk.Label(
            root,
            text="Status: Idle",
            style="Status.TLabel",
            foreground="blue"
        )
        self.status.pack(pady=5)

        # ---------- BUTTONS ----------
        btn_frame = ttk.Frame(root)
        btn_frame.pack(pady=10)

        run_btn = ttk.Button(
            btn_frame,
            text="Run Simulation",
            command=self.run_simulation,
            width=20
        )
        run_btn.grid(row=0, column=0, padx=10)

        exit_btn = ttk.Button(
            btn_frame,
            text="Exit",
            command=root.destroy,
            width=20
        )
        exit_btn.grid(row=0, column=1, padx=10)

        # ---------- OUTPUT ----------
        output_frame = ttk.LabelFrame(
            root,
            text="System Log",
            padding=10
        )
        output_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.output_text = tk.Text(
            output_frame,
            height=15,
            wrap="word",
            font=("Consolas", 10)
        )
        self.output_text.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(
            output_frame,
            orient="vertical",
            command=self.output_text.yview
        )
        scrollbar.pack(side="right", fill="y")

        self.output_text.config(yscrollcommand=scrollbar.set)

        # ---------- FOOTER ----------
        footer = ttk.Label(
            root,
            text="Developed by Malik Talha",
            font=("Segoe UI", 9),
            foreground="gray"
        )
        footer.pack(pady=5)

    # ---------- RUN SIMULATION ----------
    def run_simulation(self):
        self.output_text.delete("1.0", tk.END)
        self.status.config(
            text="Status: Running Simulation...",
            foreground="orange"
        )

        try:
            result = subprocess.run(
                ["python", "../src/main.py"],
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="ignore"
            )

            self.output_text.insert(tk.END, result.stdout)
            self.status.config(
                text="Status: Simulation Completed",
                foreground="green"
            )

        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.status.config(
                text="Status: Error",
                foreground="red"
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = DeadlockGUI(root)
    root.mainloop()
