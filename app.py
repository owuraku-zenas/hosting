from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    projects = [
        {
            'title': 'Portfolio Website',
            'description': 'Personal portfolio built with Flask and TailwindCSS.',
            'tech': ['Flask', 'TailwindCSS', 'Jinja2'],
            'link': 'https://example.com/portfolio'
        },
        {
            'title': 'Blog Platform',
            'description': 'A simple multi-user blog platform with Markdown support.',
            'tech': ['Flask', 'SQLite', 'Markdown', 'Jinja2'],
            'link': 'https://example.com/blog-platform'
        },
        {
            'title': 'Task Manager',
            'description': 'Kanban-style task manager with drag-and-drop UI.',
            'tech': ['Flask', 'JavaScript', 'HTML5', 'CSS3'],
            'link': 'https://example.com/task-manager'
        },
        {
            'title': 'Weather Dashboard',
            'description': 'Live weather dashboard using OpenWeatherMap API.',
            'tech': ['Flask', 'Requests', 'Bootstrap'],
            'link': 'https://example.com/weather-dashboard'
        },
        {
            'title': 'API Starter',
            'description': 'RESTful API boilerplate with Flask and JWT auth.',
            'tech': ['Flask', 'JWT', 'SQLite'],
            'link': 'https://example.com/api-starter'
        },
        {
            'title': 'Realtime Chat',
            'description': 'WebSocket chat app with Flask-SocketIO.',
            'tech': ['Flask', 'Socket.IO', 'Redis'],
            'link': 'https://example.com/realtime-chat'
        }
    ]
    return render_template('index.html', projects=projects)

if __name__ == '__main__':
    app.run(debug=True)
