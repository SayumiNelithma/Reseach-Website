import re

path = r'd:\SLIIT\Year 04 Semester 1\Research Project\research website\ELDEASE-WEBSITE\css\style.css'
with open(path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace hardcoded #fff or #ffffff with var(--white)
css = re.sub(r'#fff(fff)?\b', 'var(--white)', css, flags=re.IGNORECASE)

# Replace #fbfdff with var(--bg-body)
css = re.sub(r'#fbfdff\b', 'var(--bg-body)', css, flags=re.IGNORECASE)

# Add variables to :root
root_end = css.find('}')
if root_end != -1:
    new_vars = '\n  --bg-body:#fbfdff;\n  --bg-card:var(--white);\n  --border-color:#edf2f7;\n  --footer-bg:#0b1f33;\n'
    css = css[:root_end] + new_vars + css[root_end:]

# Add [data-theme='dark']
dark_theme = """
[data-theme="dark"] {
  --primary:#3b82f6;
  --primary-dark:#2563eb;
  --secondary:#22c55e;
  --dark:#f8fafc;
  --text:#94a3b8;
  --light:#1e293b;
  --lighter:#334155;
  --white:#0f172a;
  --shadow:0 12px 35px rgba(0,0,0,0.4);
  --shadow-strong:0 18px 50px rgba(0,0,0,0.6);
  --bg-body:#020617;
  --bg-card:#0f172a;
  --border-color:#334155;
  --footer-bg:#020617;
}

[data-theme="dark"] .navbar.bg-white {
  background-color: var(--white) !important;
}

[data-theme="dark"] .bg-white {
  background-color: var(--white) !important;
}

[data-theme="dark"] .bg-light {
  background-color: var(--light) !important;
}
"""

# Insert after :root block
root_end_idx = css.find('}', css.find(':root')) + 1
css = css[:root_end_idx] + dark_theme + css[root_end_idx:]

# Replace some other hardcoded colors
css = css.replace('#0b1f33', 'var(--footer-bg)')
css = css.replace('#edf2f7', 'var(--border-color)')
css = css.replace('#d6dfeb', 'var(--border-color)')
css = css.replace('#ecf1f7', 'var(--border-color)')

# Add transitions
if 'body{' in css:
    css = css.replace('body{', 'body{\n  transition: background-color 0.3s ease, color 0.3s ease;')

if '.content-card{' in css:
    css = css.replace('.content-card{', '.content-card{\n  transition: background-color 0.3s ease, color 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease;')

if '.custom-navbar{' in css:
    css = css.replace('.custom-navbar{', '.custom-navbar{\n  transition: background-color 0.3s ease, color 0.3s ease;')

# Ensure .download-card and other components have transition
css += "\n.download-card, .feature-card, .research-card, .tech-card, .team-card, .contact-card, .objective-card { transition: background-color 0.3s ease, color 0.3s ease, box-shadow 0.3s ease, transform 0.3s ease; }\n"
css += "\n[data-theme='dark'] .navbar-brand span { color: var(--dark); }\n"
css += "\n[data-theme='dark'] .text-dark { color: var(--dark) !important; }\n"
css += "\n[data-theme='dark'] .text-muted { color: var(--text) !important; }\n"
css += "\n[data-theme='dark'] .btn-outline-primary { border-color: var(--primary); color: var(--primary); }\n"
css += "\n[data-theme='dark'] .btn-outline-primary:hover { background-color: var(--primary); color: var(--white); }\n"
css += "\n[data-theme='dark'] .btn-outline-success { border-color: var(--secondary); color: var(--secondary); }\n"
css += "\n[data-theme='dark'] .btn-outline-success:hover { background-color: var(--secondary); color: var(--white); }\n"

with open(path, 'w', encoding='utf-8') as f:
    f.write(css)
print('CSS updated successfully!')
