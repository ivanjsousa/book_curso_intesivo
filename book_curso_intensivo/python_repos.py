import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


# Faz uma chamada de API e armazena a resposta
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status core:", r.status_code)


# Armazena a resposta da API em uma variável
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# Explora informações sobre os repositórios
repo_dicts = response_dict['items']

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# Cria a visualização
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Projetos Python com mais estrelas no GitHub'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_respo.svg')
