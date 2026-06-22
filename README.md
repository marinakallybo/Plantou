# 🌱 PéDeQuê?

**PéDeQuê?** é uma aplicação web desenvolvida em **Python** e **Django** para apoiar pequenos produtores e agricultores familiares na escolha de culturas mais adequadas para plantio.

A proposta do projeto é transformar informações como **temperatura**, **tipo de solo** e **umidade** em recomendações simples e acessíveis, ajudando o usuário a entender quais culturas possuem maior compatibilidade com as condições informadas.

---

## 📌 Objetivo do projeto

Muitos pequenos produtores precisam tomar decisões sobre o que plantar considerando clima, solo, disponibilidade de recursos e custo. O **PéDeQuê?** nasce como uma ferramenta inicial para apoiar essa tomada de decisão.

Nesta primeira versão, o sistema permite:

* Cadastrar culturas agrícolas em um banco de dados;
* Importar culturas automaticamente a partir de um arquivo CSV;
* Listar culturas cadastradas;
* Gerar recomendações com base em temperatura, solo e umidade;
* Exibir uma pontuação de compatibilidade para cada cultura recomendada.

Futuramente, a ideia é evoluir o projeto para uma plataforma mais completa, com integração a APIs climáticas, preços médios de sementes, fornecedores, conteúdos educativos e ferramentas para agricultura familiar.

---

## 🚀 Funcionalidades atuais

* ✅ Aplicação web com Django;
* ✅ Banco de dados com culturas agrícolas;
* ✅ Importação de culturas via CSV;
* ✅ Página de listagem de culturas;
* ✅ Página de recomendação de culturas;
* ✅ Cálculo de compatibilidade com base em regras;
* ✅ Interface estilizada com HTML e CSS;
* ✅ Estrutura inicial preparada para futuras integrações.

---

## 🧠 Como funciona a recomendação?

O usuário informa:

* Temperatura média;
* Tipo de solo;
* Umidade.

A aplicação compara essas informações com as condições ideais cadastradas para cada cultura.

A pontuação inicial segue a lógica:

| Critério                          |  Pontuação |
| --------------------------------- | ---------: |
| Temperatura dentro da faixa ideal | +40 pontos |
| Solo compatível                   | +30 pontos |
| Umidade compatível                | +30 pontos |

A partir disso, o sistema ordena as culturas pela maior pontuação e exibe as melhores recomendações.

---

## 🛠️ Tecnologias utilizadas

* Python
* Django
* SQLite
* HTML
* CSS
* CSV
* Git e GitHub

---

## 📁 Estrutura do projeto

```text
AgroSeed/
│
├── agroseed/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── recomendador/
│   ├── management/
│   │   └── commands/
│   │       └── importar_culturas.py
│   ├── migrations/
│   ├── static/
│   │   └── recomendador/
│   │       └── css/
│   │           └── style.css
│   ├── templates/
│   │   └── recomendador/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── listar_culturas.html
│   │       └── recomendar.html
│   ├── admin.py
│   ├── models.py
│   ├── services.py
│   ├── urls.py
│   └── views.py
│
├── data/
│   └── culturas.csv
│
├── manage.py
├── .gitignore
├── LICENSE
└── README.md
```

---

## ⚙️ Como rodar o projeto localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

Entre na pasta do projeto:

```bash
cd seu-repositorio
```

---

### 2. Crie o ambiente virtual

```bash
python -m venv venv
```

Ative o ambiente virtual no Windows PowerShell:

```bash
.\venv\Scripts\Activate.ps1
```

Caso o PowerShell bloqueie a ativação, execute:

```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Depois tente ativar novamente:

```bash
.\venv\Scripts\Activate.ps1
```

---

### 3. Instale as dependências

```bash
pip install django
```

Se o projeto tiver um arquivo `requirements.txt`, utilize:

```bash
pip install -r requirements.txt
```

---

### 4. Aplique as migrações

```bash
python manage.py migrate
```

---

### 5. Importe as culturas do CSV

```bash
python manage.py importar_culturas
```

Esse comando lê o arquivo:

```text
data/culturas.csv
```

E cadastra ou atualiza as culturas no banco de dados.

---

### 6. Rode o servidor

```bash
python manage.py runserver
```

Acesse no navegador:

```text
http://127.0.0.1:8000/
```

---

## 🌾 Páginas principais

| Página         | Descrição                       |
| -------------- | ------------------------------- |
| `/`            | Página inicial do projeto       |
| `/culturas/`   | Lista de culturas cadastradas   |
| `/recomendar/` | Formulário de recomendação      |
| `/admin/`      | Painel administrativo do Django |

---

## 🧪 Exemplo de uso

O usuário informa:

```text
Temperatura: 23°C
Solo: argiloso
Umidade: média
```

O sistema pode retornar recomendações como:

```text
Alface — 100% compatível
Couve — 100% compatível
Tomate — 100% compatível
Feijão — 100% compatível
Milho — 100% compatível
```

Cada resultado apresenta informações como:

* Descrição da cultura;
* Temperatura ideal;
* Tipo de solo ideal;
* Umidade ideal;
* Época de plantio;
* Tempo médio de colheita;
* Dificuldade de cultivo;
* Motivos da recomendação.

---

## 📊 Dados utilizados

Atualmente, os dados das culturas são armazenados em um arquivo CSV local.

Cada cultura possui informações como:

* Nome;
* Descrição;
* Temperatura mínima;
* Temperatura máxima;
* Solo ideal;
* Umidade ideal;
* Época de plantio;
* Tempo de colheita;
* Dificuldade.

Em versões futuras, a base de dados poderá ser enriquecida com fontes externas e APIs públicas.

---

## 🔮 Próximas melhorias

* [ ] Melhorar a lógica de pontuação da recomendação;
* [ ] Considerar temperaturas próximas da faixa ideal;
* [ ] Permitir busca por cidade ou região;
* [ ] Integrar API climática para obter temperatura e umidade automaticamente;
* [ ] Adicionar preço médio de sementes como fator de recomendação;
* [ ] Criar histórico de consultas;
* [ ] Adicionar imagens das culturas;
* [ ] Criar filtros por dificuldade, tempo de colheita e época de plantio;
* [ ] Criar área educativa com conteúdos para pequenos produtores;
* [ ] Evoluir para uma plataforma/hub de ferramentas agro.

---

## 💡 Visão futura

A ideia do **PéDeQuê?** é crescer além de um recomendador de culturas.

No futuro, a plataforma poderá reunir:

* Consulta climática por região;
* Comparação de preços de sementes;
* Indicação de fornecedores;
* Fórum para pequenos produtores;
* Blog educativo;
* Calendário de plantio;
* Ferramentas de apoio à agricultura familiar.
