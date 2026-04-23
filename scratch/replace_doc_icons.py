import os

path = r'd:\SLIIT\Year 04 Semester 1\Research Project\research website\ELDEASE-WEBSITE\index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    '<h5><i class="fas fa-file-pdf me-2"></i>Topic Assessment</h5>': '<h5><i class="fas fa-file-alt text-primary me-2"></i>Topic Assessment</h5>',
    '<h5><i class="fas fa-file-pdf me-2"></i>Project Charter</h5>': '<h5><i class="fas fa-file-signature text-success me-2"></i>Project Charter</h5>',
    '<h5><i class="fas fa-file-pdf me-2"></i>Project Proposal</h5>': '<h5><i class="fas fa-file-pdf text-danger me-2"></i>Project Proposal</h5>',
    '<h5><i class="fas fa-file-pdf me-2"></i>Status Documents I</h5>': '<h5><i class="fas fa-file-alt text-info me-2"></i>Status Documents I</h5>',
    '<h5><i class="fas fa-file-pdf me-2"></i>Status Documents II</h5>': '<h5><i class="fas fa-file-alt text-info me-2"></i>Status Documents II</h5>',
    '<h5><i class="fas fa-file-pdf me-2"></i>Research Paper</h5>': '<h5><i class="fas fa-file-contract text-danger me-2"></i>Research Paper</h5>',
    '<h5><i class="fas fa-file-pdf me-2"></i>Final Report</h5>': '<h5><i class="fas fa-book text-primary me-2"></i>Final Report</h5>',
    '<h5><i class="fas fa-file-image me-2"></i>Poster</h5>': '<h5><i class="fas fa-image text-secondary me-2"></i>Poster</h5>',
    '<h5><i class="fas fa-file-powerpoint me-2"></i>Project Proposal</h5>': '<h5><i class="fas fa-file-powerpoint text-warning me-2"></i>Project Proposal</h5>',
    '<h5><i class="fas fa-file-powerpoint me-2"></i>Progress Presentation I</h5>': '<h5><i class="fas fa-chart-line text-info me-2"></i>Progress Presentation I</h5>',
    '<h5><i class="fas fa-file-powerpoint me-2"></i>Progress Presentation II</h5>': '<h5><i class="fas fa-chart-bar text-info me-2"></i>Progress Presentation II</h5>',
    '<h5><i class="fas fa-file-powerpoint me-2"></i>Final Presentation</h5>': '<h5><i class="fas fa-file-powerpoint text-primary me-2"></i>Final Presentation</h5>'
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated index.html with colorful document icons')
