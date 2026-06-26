# 🌱 PéDeQuê?

**PéDeQuê?** é uma aplicação web desenvolvida com **Python** e **Django** para apoiar pequenos produtores e agricultores familiares na escolha de culturas mais adequadas para plantio.

A plataforma recomenda culturas com base em condições como **temperatura**, **tipo de solo** e **umidade**, apresentando uma pontuação de compatibilidade e explicando os motivos por trás de cada recomendação.

> A ideia central do projeto é responder, de forma simples e acessível:
> **“Com essas condições, pé de quê eu posso plantar?”**

---

## 📌 Status do projeto

🚧 Projeto em desenvolvimento.

Atualmente, o sistema já possui:

* Banco de culturas agrícolas;
* Importação de culturas via CSV;
* Página inicial estilizada;
* Listagem de culturas cadastradas;
* Formulário de recomendação;
* Cálculo de compatibilidade baseado em regras;
* Interface web com HTML e CSS;
* Estrutura preparada para futuras integrações com APIs.

---

## 🎯 Problema

Pequenos produtores muitas vezes precisam decidir o que plantar considerando diferentes fatores, como clima, solo, umidade, época de plantio, custo e tempo de colheita.

Essa decisão pode ser difícil quando as informações estão espalhadas, são muito técnicas ou não estão adaptadas à realidade da agricultura familiar.

---

## 💡 Solução proposta

O **PéDeQuê?** propõe uma ferramenta simples para transformar dados agrícolas em recomendações compreensíveis.

Na primeira versão, o usuário informa:

* Temperatura média;
* Tipo de solo;
* Umidade.

Com base nesses dados, o sistema compara as condições informadas com as características ideais de cada cultura cadastrada no banco e retorna as opções mais compatíveis.

---

## ✨ Funcionalidades

### Página inicial

Apresenta a proposta do projeto e direciona o usuário para as principais funcionalidades.

### Listagem de culturas

Exibe as culturas cadastradas no banco, mostrando informações como temperatura ideal, solo, umidade, época de plantio, tempo de colheita e dificuldade.

### Recomendador de culturas

Permite que o usuário informe as condições do plantio e receba uma lista de culturas recomendadas com pontuação de compatibilidade.

### Importação via CSV

As culturas podem ser cadastradas em massa por meio de um arquivo CSV, facilitando a manutenção e expansão da base de dados.

### Painel administrativo

O projeto utiliza o Django Admin para gerenciar culturas cadastradas no banco de dados.

---

## 🛠️ Tecnologias utilizadas

* **Python**
* **Django**
* **SQLite**
* **HTML**
* **CSS**
* **CSV**
* **Git e GitHub**

---

## 🗂️ Estrutura do projeto

```text
PéDeQuê/
│
├── plantou/
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

> Observação: `plantou/` é a pasta técnica de configuração do projeto Django. O nome público da aplicação é **PéDeQuê?**.

---

## 📊 Dados utilizados

Atualmente, os dados das culturas estão armazenados localmente no arquivo:

```text
data/culturas.csv
```

Cada registro contém informações como:

| Campo                 | Descrição                       |
| --------------------- | ------------------------------- |
| `nome`                | Nome da cultura                 |
| `descricao`           | Descrição geral da cultura      |
| `temperatura_minima`  | Temperatura mínima recomendada  |
| `temperatura_maxima`  | Temperatura máxima recomendada  |
| `solo_ideal`          | Tipo de solo mais adequado      |
| `umidade_ideal`       | Umidade recomendada             |
| `epoca_plantio`       | Melhor época de plantio         |
| `tempo_colheita_dias` | Tempo médio até a colheita      |
| `dificuldade`         | Nível de dificuldade do cultivo |

A base de culturas é importada para o banco usando um comando customizado do Django.

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

Caso exista um arquivo `requirements.txt`, utilize:

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

Esse comando lê o arquivo `data/culturas.csv` e cadastra ou atualiza as culturas no banco de dados.

---

### 6. Rode o servidor local

```bash
python manage.py runserver
```

Acesse no navegador:

```text
http://127.0.0.1:8000/
```

---

## 🌐 Rotas principais

| Rota           | Descrição                       |
| -------------- | ------------------------------- |
| `/`            | Página inicial                  |
| `/culturas/`   | Lista de culturas cadastradas   |
| `/recomendar/` | Formulário de recomendação      |
| `/admin/`      | Painel administrativo do Django |

---

## 🖼️ Interface

<img width="1872" height="931" alt="image" src="https://github.com/user-attachments/assets/0e74a363-a331-43cb-ab65-749ffaa46ee6" />

---

## 🔮 Roadmap

### Melhorias planejadas para o MVP

* [ ] Melhorar a lógica de pontuação da recomendação;
* [ ] Considerar temperaturas próximas da faixa ideal;
* [ ] Exibir apenas as melhores recomendações;
* [ ] Criar histórico de consultas;
* [ ] Adicionar filtros por dificuldade, tempo de colheita e época de plantio;
* [ ] Adicionar imagens ou ícones para as culturas;
* [ ] Melhorar a responsividade da interface.

### Integrações futuras

* [ ] Permitir busca por cidade ou região;
* [ ] Integrar API climática para obter temperatura e umidade automaticamente;
* [ ] Adicionar preço médio de sementes como fator de recomendação;
* [ ] Criar estrutura para fornecedores e preços;
* [ ] Explorar dados públicos e APIs agrícolas.

### Visão de plataforma

* [ ] Criar área educativa com conteúdos para pequenos produtores;
* [ ] Criar calendário de plantio;
* [ ] Criar fórum ou espaço de troca entre produtores;
* [ ] Evoluir para um hub de ferramentas voltadas à agricultura familiar.

---

## 🌱 Visão futura

A ideia do **PéDeQuê?** é crescer além de um recomendador de culturas.

No futuro, a plataforma poderá reunir dados climáticos, preços de sementes, fornecedores, conteúdos educativos e ferramentas comunitárias em um único ambiente para apoiar pequenos produtores do plantio à colheita.

Possíveis módulos futuros:

* **PéDeQuê? Clima** — consulta climática por região;
* **PéDeQuê? Mercado** — comparação de preços de sementes;
* **PéDeQuê? Aprenda** — conteúdos educativos;
* **PéDeQuê? Comunidade** — troca de experiências entre produtores;
* **PéDeQuê? Fornecedores** — conexão com vendedores e pequenos empreendedores.

---

## 👩‍💻 Desenvolvido por

Desenvolvido por **Marina Kally Bernardo de Oliveira** como projeto de estudo em desenvolvimento web com Python, Django, banco de dados e construção de aplicações orientadas a dados.

---

## 📄 Licença

Este projeto está licenciado sob a licença MIT.

As bases de dados, APIs ou fontes externas integradas futuramente pertencem aos seus respectivos provedores e devem seguir seus próprios termos de uso.
