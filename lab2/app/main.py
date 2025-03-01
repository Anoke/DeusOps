from flask import Blueprint, render_template_string

main = Blueprint('main', __name__)

@main.route('/')
def index():
    html = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
      <meta charset="UTF-8">
      <title>Крутящийся кот</title>
      <style>
        @keyframes spin {
          from { transform: rotate(0deg); }
          to { transform: rotate(360deg); }
        }
        .rotating-cat {
          animation: spin 4s linear infinite;
          width: 300px;
          height: 300px;
          display: block;
          margin: 0 auto;
        }
        body {
          text-align: center;
          font-family: Arial, sans-serif;
          background-color: #f0f0f0;
        }
      </style>
    </head>
    <body>
      <h1>Вот крутящийся кот!</h1>
      <svg class="rotating-cat" width="300" height="300" viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
        <!-- Фон -->
        <rect width="100%" height="100%" fill="#f0f0f0"/>
        
        <!-- Голова кота -->
        <circle cx="200" cy="200" r="80" fill="#F4D03F" stroke="black" stroke-width="3"/>
        
        <!-- Уши -->
        <polygon points="140,120 170,60 200,120" fill="#F4D03F" stroke="black" stroke-width="3"/>
        <polygon points="260,120 230,60 200,120" fill="#F4D03F" stroke="black" stroke-width="3"/>
        
        <!-- Глаза -->
        <circle cx="170" cy="190" r="10" fill="black"/>
        <circle cx="230" cy="190" r="10" fill="black"/>
        
        <!-- Нос -->
        <polygon points="200,210 190,230 210,230" fill="red"/>
        
        <!-- Рот -->
        <path d="M190,240 Q200,250 210,240" stroke="black" stroke-width="2" fill="none"/>
        
        <!-- Усы -->
        <line x1="130" y1="220" x2="170" y2="220" stroke="black" stroke-width="2"/>
        <line x1="230" y1="220" x2="270" y2="220" stroke="black" stroke-width="2"/>
        
        <!-- Бутылочка "Vodka" -->
        <rect x="280" y="240" width="20" height="60" fill="#A3E4D7" stroke="black" stroke-width="2"/>
        <line x1="280" y1="240" x2="300" y2="240" stroke="black" stroke-width="2"/>
        <text x="275" y="315" font-size="12" fill="black">Vodka</text>
        
        <!-- Лапка кота, тянущаяся к бутылке -->
        <path d="M250,240 Q270,260 280,240" stroke="black" stroke-width="2" fill="none"/>
      </svg>
    </body>
    </html>
    """
    return render_template_string(html)
