import os

path = r'd:\SLIIT\Year 04 Semester 1\Research Project\research website\ELDEASE-WEBSITE\js\script.js'
with open(path, 'r', encoding='utf-8') as f:
    js = f.read()

theme_logic = """
  // Theme Toggle Logic
  const themeToggle = document.getElementById('themeToggle');
  const themeIcon = document.getElementById('themeIcon');
  const currentTheme = localStorage.getItem('theme');

  if (currentTheme) {
    document.documentElement.setAttribute('data-theme', currentTheme);
    if (themeIcon) {
      if (currentTheme === 'dark') {
        themeIcon.classList.replace('fa-moon', 'fa-sun');
      } else {
        themeIcon.classList.replace('fa-sun', 'fa-moon');
      }
    }
  }

  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      let theme = document.documentElement.getAttribute('data-theme');
      if (theme === 'dark') {
        document.documentElement.setAttribute('data-theme', 'light');
        localStorage.setItem('theme', 'light');
        themeIcon.classList.replace('fa-sun', 'fa-moon');
      } else {
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('theme', 'dark');
        themeIcon.classList.replace('fa-moon', 'fa-sun');
      }
    });
  }
"""

if '// Theme Toggle Logic' not in js:
    # insert before the end of DOMContentLoaded callback
    idx = js.rfind('});')
    if idx != -1:
        js = js[:idx] + theme_logic + js[idx:]

with open(path, 'w', encoding='utf-8') as f:
    f.write(js)
print('JS updated successfully!')
