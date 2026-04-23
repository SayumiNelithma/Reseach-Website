import os
import glob

path_dir = r'd:\SLIIT\Year 04 Semester 1\Research Project\research website\ELDEASE-WEBSITE'
html_files = glob.glob(os.path.join(path_dir, '*.html'))

toggle_button = """
        <li class="nav-item ms-lg-3 d-flex align-items-center">
          <button id="themeToggle" class="btn btn-outline-secondary btn-sm rounded-circle" aria-label="Toggle Theme" style="width: 36px; height: 36px;">
            <i id="themeIcon" class="fas fa-moon"></i>
          </button>
        </li>
"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'id="themeToggle"' in content:
        continue
    
    # Insert before </ul>
    idx = content.find('</ul>')
    if idx != -1:
        # Check if we are inside the navbar collapse
        navbar_idx = content.rfind('<div class="collapse navbar-collapse"', 0, idx)
        if navbar_idx != -1:
            content = content[:idx] + toggle_button + content[idx:]
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Updated {os.path.basename(file)}')

print('Done updating HTML files.')
