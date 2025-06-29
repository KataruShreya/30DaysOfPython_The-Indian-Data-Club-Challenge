import json
import os
import matplotlib.pyplot as plt
from kivy.app import App
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.clock import Clock
from fpdf import FPDF

Window.size = (600, 600)
Window.clearcolor = get_color_from_hex("#FDF6EC")

TARGET_LEVELS = {
    "Data Analyst": {"Excel": 10, "SQL": 10, "Power BI": 10, "Python": 10},
    "Data Scientist": {"Python (Pandas/Numpy etc)": 10, "Machine Learning (Scikit-learn)": 10, "Statistics": 10, "Deep Learning": 10},
    "Data Engineer": {"SQL": 10, "Apache Spark": 10, "Cloud Storage": 10},
    "Machine Learning Engineer": {"Python": 10, "TensorFlow/PyTorch": 10, "Model Deployment": 10, "Docker": 10},
    "Cloud Engineer": {"AWS/GCP/Azure": 10, "Docker": 10, "Linux": 10, "CI/CD": 10},
    "Backend Developer": {"Python/Node.js": 10, "Django/Express": 10, "SQL/NoSQL": 10, "REST API Design": 10, "Authentication": 10},
    "Frontend Developer": {"HTML/CSS": 10, "JavaScript": 10, "React/Angular": 10, "Redux/Context": 10, "Testing": 10},
    "Cybersecurity Analyst": {"Network Protocols": 10, "Security Tools": 10, "Linux": 10, "Python": 10, "Threat Detection": 10},
    "UI/UX Designer": {"Figma/XD": 10, "Design Systems": 10, "User Testing": 10, "Accessibility": 10, "UX Writing": 10},
    "Product Manager": {"Agile/Scrum": 10, "Wireframing": 10, "Stakeholder Management": 10, "Analytics Tools": 10, "Roadmapping": 10}
}

class SkillGapApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=15, spacing=10, **kwargs)
        self.roles_data = self.load_json("roles.json")
        self.roadmaps = self.load_json("roadmaps.json")
        self.user_inputs = {}
        self.latest_user = None
        self.build_ui()

    def load_json(self, filename):
        if os.path.exists(filename):
            with open(filename, "r") as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return {}
        return {}

    def build_ui(self):
        self.add_widget(Label(text="SKILL GAP ANALYZER", font_size=26, bold=True, size_hint_y=None, height=50, color=get_color_from_hex("#5C4033")))

        self.name_input = TextInput(hint_text="Enter your name", size_hint_y=None, height=40, background_color=get_color_from_hex("#F5E8C7"))
        self.status_input = TextInput(hint_text="Student / Working", size_hint_y=None, height=40, background_color=get_color_from_hex("#F5E8C7"))
        self.role_spinner = Spinner(text="Select Aspiring Role", values=list(self.roles_data.keys()), size_hint_y=None, height=44,
                                     background_color=get_color_from_hex("#E7A977"), color=get_color_from_hex("#FFFFFF"))
        self.role_spinner.bind(text=self.on_role_select)

        self.skills_layout = GridLayout(cols=2, spacing=10, size_hint_y=None)
        self.skills_layout.bind(minimum_height=self.skills_layout.setter('height'))
        scroll = ScrollView()
        scroll.add_widget(self.skills_layout)

        self.submit_btn = Button(text="Submit", size_hint_y=None, height=50,
                                 background_color=get_color_from_hex("#E7A977"), color=get_color_from_hex("#FFFFFF"))
        self.submit_btn.bind(on_press=self.on_submit)

        self.pdf_btn = Button(text="Download PDF", size_hint_y=None, height=50,
                              background_color=get_color_from_hex("#E7A977"), color=get_color_from_hex("#FFFFFF"))
        self.pdf_btn.bind(on_press=self.generate_pdf)
        self.pdf_btn.disabled = True

        self.add_widget(self.name_input)
        self.add_widget(self.status_input)
        self.add_widget(self.role_spinner)
        self.add_widget(scroll)
        self.add_widget(self.submit_btn)
        self.add_widget(self.pdf_btn)

    def on_role_select(self, spinner, role):
        self.skills_layout.clear_widgets()
        self.user_inputs.clear()
        for skill, desc in self.roles_data[role].items():
            self.skills_layout.add_widget(Label(text=f"{skill}: {desc}", size_hint_y=None, height=40, color=get_color_from_hex("#000000")))
            rating_layout = BoxLayout(orientation='horizontal', spacing=5, size_hint_y=None, height=40)
            rating_input = TextInput(text="0", input_filter='int', multiline=False, size_hint=(None, 1), width=40,
                                     halign="center", background_color=get_color_from_hex("#E2E8C0"))
            inc_btn = Button(text="+", size_hint=(None, 1), width=30, background_color=get_color_from_hex("#000000"), color=get_color_from_hex("#FFFFFF"))
            dec_btn = Button(text="-", size_hint=(None, 1), width=30, background_color=get_color_from_hex("#000000"), color=get_color_from_hex("#FFFFFF"))
            inc_btn.bind(on_press=lambda x, inp=rating_input: self.adjust_rating(inp, 1))
            dec_btn.bind(on_press=lambda x, inp=rating_input: self.adjust_rating(inp, -1))
            rating_layout.add_widget(dec_btn)
            rating_layout.add_widget(rating_input)
            rating_layout.add_widget(inc_btn)
            self.user_inputs[skill] = rating_input
            self.skills_layout.add_widget(rating_layout)

    def adjust_rating(self, input_widget, change):
        try:
            val = int(input_widget.text)
        except ValueError:
            val = 1
        new_val = max(1, min(10, val + change))
        input_widget.text = str(new_val)

    def on_submit(self, instance):
        if not self.name_input.text or not self.status_input.text or self.role_spinner.text == "Select Aspiring Role":
            self.show_popup_with_button("Please complete all fields.")
            return
        user_data = {
            "name": self.name_input.text,
            "status": self.status_input.text,
            "aspiring_role": self.role_spinner.text,
            "skills": {k: int(v.text) for k, v in self.user_inputs.items()}
        }
        self.save_user(user_data)
        self.latest_user = user_data
        self.create_chart(user_data)
        self.show_popup_with_button("Skill gap chart saved!\nClick 'Download PDF' to generate your roadmap.")
        self.pdf_btn.disabled = False

    def save_user(self, user_data):
        data = self.load_json("users.json")
        if not isinstance(data, list):
            data = []
        data.append(user_data)
        with open("users.json", "w") as f:
            json.dump(data, f, indent=2)

    def create_chart(self, user_data):
        role = user_data["aspiring_role"]
        targets = TARGET_LEVELS.get(role, {})
        skills = list(targets.keys())
        self_ratings = [user_data["skills"].get(s, 0) for s in skills]
        target_ratings = [targets[s] for s in skills]
        x = range(len(skills))
        plt.figure(figsize=(10, 7))
        plt.bar([i - 0.2 for i in x], self_ratings, width=0.4, label="Your Rating", color="#A8E0DF")
        plt.bar([i + 0.2 for i in x], target_ratings, width=0.4, label="Target", color="#F4C2E2")
        plt.xticks(x, skills, rotation=45, ha='right')
        plt.ylabel("Skill Level")
        plt.ylim(0, 10)
        plt.title(f"Skill Gap: {user_data['name']} ({role})")
        plt.legend()
        plt.tight_layout()
        plt.savefig("skill_gap_chart.png")
        plt.close()

    def generate_pdf(self, instance):
        user = self.latest_user
        role = user["aspiring_role"]
        pdf = FPDF()

        # Page 1 – Chart
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, "SKILL GAP ROADMAP", ln=True, align="C")
        pdf.ln(10)
        if os.path.exists("skill_gap_chart.png"):
            pdf.image("skill_gap_chart.png", x=10, w=180)

        # Page 2 – Table
        pdf.add_page()
        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, f"Skill Gap Table: {user['name']} - {role}", ln=True, align="C")
        pdf.ln(5)
        pdf.set_font("Arial", "B", 12)
        pdf.cell(60, 10, "Skill", border=1)
        pdf.cell(20, 10, "Self", border=1)
        pdf.cell(20, 10, "Target", border=1)
        pdf.cell(20, 10, "Gap", border=1)
        pdf.cell(70, 10, "Suggestion", border=1)
        pdf.ln()
        pdf.set_font("Arial", "", 12)
        for skill, rating in user["skills"].items():
            target = TARGET_LEVELS[role].get(skill, 10)
            gap = max(0, target - rating)
            suggestion = self.get_suggestion(rating)
            pdf.cell(60, 10, skill, border=1)
            pdf.cell(20, 10, str(rating), border=1)
            pdf.cell(20, 10, str(target), border=1)
            pdf.cell(20, 10, str(gap), border=1)
            pdf.multi_cell(70, 10, suggestion, border=1)

        # Page 3 – Roadmap
        pdf.add_page()
        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, "Your Personalized 3-Month Roadmap", ln=True, align="C")
        pdf.ln(5)
        roadmap = self.roadmaps.get(role, "No roadmap available.")
        pdf.set_font("Arial", "", 12)
        pdf.multi_cell(0, 8, roadmap)
        pdf.ln(10)
        pdf.set_font("Arial", "I", 10)
        pdf.cell(0, 10, "Generated by Skill Gap Analyzer v1.0", ln=True, align="C")

        pdf.output("Skill_Roadmap.pdf")
        self.show_popup("PDF saved as Skill_Roadmap.pdf")

    def get_suggestion(self, rating):
        if rating <= 3:
            return "A lot of improvement is needed but nothing is impossible."
        elif 4 <= rating <= 7:
            return "You are almost there... Just need a little more practice."
        elif rating >= 8:
            return "Woohoo! You're almost a legend here. Keep practicing!"
        return "Invalid rating."

    def show_popup(self, message, timeout=2):
        popup = Popup(title="Skill Gap Analyzer", content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()
        Clock.schedule_once(lambda dt: popup.dismiss(), timeout)

    def show_popup_with_button(self, message):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        label = Label(text=message, halign="center", valign="middle")
        btn = Button(text="OK", size_hint=(1, None), height=40, background_color=get_color_from_hex("#E7A977"), color=get_color_from_hex("#FFFFFF"))
        popup = Popup(title="Skill Gap Analyzer", content=layout, size_hint=(None, None), size=(400, 200))
        btn.bind(on_press=popup.dismiss)
        layout.add_widget(label)
        layout.add_widget(btn)
        popup.open()

class MyApp(App):
    def build(self):
        return SkillGapApp()

if __name__ == '__main__':
    MyApp().run()
