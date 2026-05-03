import re
import random

css = """
        .section-title {
            text-align: center;
            font-family: Times New Roman;
            margin-top: 60px;
            font-size: 32px;
        }

        .carousel {
            width: 80%;
            margin: 0 auto 50px auto;
            position: relative;
        }

        .carousel-inner {
            display: flex;
            overflow-x: auto;
            scroll-snap-type: x mandatory;
            scroll-behavior: smooth;
            gap: 20px;
            padding-bottom: 20px;
            scrollbar-width: none;
        }
        
        .carousel-inner::-webkit-scrollbar {
            display: none;
        }

        .slide {
            flex: 0 0 100%;
            scroll-snap-align: center;
            display: flex;
            justify-content: flex-start;
            gap: 20px;
        }

        .project-card {
            background-color: darkblue;
            border-radius: 15px;
            padding: 20px;
            flex: 1 1 0; 
            aspect-ratio: 1 / 1.1;
            color: white;
            text-align: center;
            font-family: Times New Roman;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            box-sizing: border-box;
        }

        .project-card h3 {
            color: yellow;
            margin-top: 0;
            font-size: 20px;
            margin-bottom: 10px;
        }

        .project-card p {
            font-size: 14px;
            margin-bottom: 15px;
        }

        .progress-bar-container {
            width: 90%;
            height: 10px;
            background-color: rgb(53, 82, 82);
            border-radius: 5px;
            margin-bottom: 5px;
            overflow: hidden;
        }

        .progress-bar-fill {
            height: 100%;
            background-color: yellow;
        }

        .progress-text {
            font-size: 14px;
            color: yellow;
            margin-bottom: 15px;
            font-weight: bold;
        }

        .project-card button {
            background-color: yellow;
            margin: 0;
            width: 130px;
            margin-top: auto;
            border-radius: 10px;
            padding: 10px;
            border: none;
        }

        .project-card button a {
            color: darkblue;
            text-decoration: none;
            font-weight: bold;
        }

        .carousel-nav {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-top: 10px;
        }

        .carousel-nav a {
            display: inline-block;
            width: 35px;
            height: 35px;
            background-color: rgb(53, 82, 82);
            color: white;
            text-align: center;
            line-height: 35px;
            border-radius: 50%;
            text-decoration: none;
            font-weight: bold;
            font-family: Arial, sans-serif;
        }

        .carousel-nav a:hover {
            background-color: darkblue;
        }
    </style>
"""

categories = {
    "Research and Journals": [
        "Quantum Computing Advances", "Ocean Acidification Study", "Microplastics in Rainwater",
        "Cognitive Behavioral Models", "Graphene Solar Panels", "AI in Medical Diagnoses"
    ],
    "Inventions": [
        "Smart Water Purifier", "Portable Wind Turbine", "Biodegradable Plastic",
        "Magnetic Levitation Skateboard", "Automated Vertical Farm", "Low-Cost Prosthetics"
    ],
    "Books": [
        "The Martian Frontier", "Chronicles of the Deep", "Urban Gardening Guide",
        "History of Modern Skateboarding", "Understanding AI Ethics", "Poetry of the Cosmos"
    ],
    "Screenplays": [
        "Echoes of Tomorrow", "The Last Detective", "A Summer in Manila",
        "Neon City Lights", "Silent Symphony", "Journey to the Center"
    ]
}

html = """
    </p>
    
"""

for cat, titles in categories.items():
    prefix = cat.split()[0].lower()
    html += f'    <h2 class="section-title">{cat}</h2>\n'
    html += '    <div class="carousel">\n'
    html += '        <div class="carousel-inner">\n'
    
    # 6 items = 3 per slide -> 2 slides
    html += f'            <div class="slide" id="{prefix}-slide-1">\n'
    for i in range(3):
        funded = random.randint(10, 95)
        html += f'''                <div class="project-card">
                    <h3>{titles[i]}</h3>
                    <p>Support this amazing project towards completion.</p>
                    <div class="progress-bar-container">
                        <div class="progress-bar-fill" style="width: {funded}%;"></div>
                    </div>
                    <div class="progress-text">{funded}% Funded</div>
                    <button><a href="#">View</a></button>
                </div>\n'''
    html += '            </div>\n'
    
    html += f'            <div class="slide" id="{prefix}-slide-2">\n'
    for i in range(3, 6):
        funded = random.randint(10, 95)
        html += f'''                <div class="project-card">
                    <h3>{titles[i]}</h3>
                    <p>Support this amazing project towards completion.</p>
                    <div class="progress-bar-container">
                        <div class="progress-bar-fill" style="width: {funded}%;"></div>
                    </div>
                    <div class="progress-text">{funded}% Funded</div>
                    <button><a href="#">View</a></button>
                </div>\n'''
    html += '            </div>\n'
    
    html += '        </div>\n'
    html += '        <div class="carousel-nav">\n'
    html += f'            <a href="#{prefix}-slide-1">1</a>\n'
    html += f'            <a href="#{prefix}-slide-2">2</a>\n'
    html += '        </div>\n'
    html += '    </div>\n\n'

html += "</body>\n</html>"

with open("projects.html", "r") as f:
    text = f.read()

text = text.replace("</style>", css, 1)

text = re.sub(r'<br> ranging from science to the arts.*', '<br> ranging from science to the arts' + html, text, flags=re.DOTALL)

with open("projects.html", "w") as f:
    f.write(text)
