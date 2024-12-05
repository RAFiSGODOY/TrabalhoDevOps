# **Documentação do Projeto**

**Autor**: Rafael Godoy Pinguelo  
**RA**: 227298-7  

## **Descrição**

Este projeto provisiona automaticamente um ambiente de monitoramento usando o Grafana, configurado para exibir um dashboard que monitora requisições de um servidor Prometheus. A automação inclui a integração com Jenkins para gerenciamento do pipeline de execução.

---

## **Pré-requisitos**

1. **Jenkins** instalado e em execução.
2. **Docker** e **Docker Compose** configurados no ambiente do Jenkins.
3. Acesso ao navegador para visualizar o Grafana no endereço `http://localhost:3000`.
4. Acesso ao navegador para visualizar o Prometheus no endereço `http://localhost:9090`.
5. Acesso ao navegador para visualizar o Jenkins no endereço `http://localhost:8080`.

---

## **Passos para Configurar e Executar o Projeto**

### **1. Iniciar o Jenkins**
   - Certifique-se de que o Jenkins está em execução. Normalmente, ele estará disponível em `http://localhost:8080`.

---

### **2. Criar uma Nova Pipeline no Jenkins**

1. **Acessar o Jenkins**
   - Vá até o Jenkins em `http://localhost:8080` e faça login.

   **Tela Inicial do Jenkins:**
   ![alt text](image.png)

2. **Criar um Novo Item**
   - Clique em **"Nova Tarefa"**.
   - Digite um nome para o pipeline, como `Pipeline-Grafana`.
   - Selecione a opção **"Pipeline"** e clique em **"OK"**.

   **Tela de criação de Pipeline:**
    ![alt text](image-1.png)

3. **Configurar o Pipeline**
   - Na página de configuração do pipeline:
     - Role até a seção **Build Triggers** e selecione **Consultar periodicamente o SCM**.
     - Adicione o seguinte texto para que o Jenkins verifique o repositório periodicamente: `H/5 * * * *`.
     - Role até a seção **Pipeline** e selecione a opção **Pipeline Script from SCM**.

   **Tela de configuração de Pipeline:**
   ![alt text](image-2.png)

4. **Configurar Repositório SCM**
   - Em **SCM**, selecione **Git**.
   - Insira o repositório Git onde o projeto está hospedado: `https://github.com/GabNasci/trabalho-devops-2397834.git`.
   - Configure as credenciais, se necessário.
   - Clique em **Salvar**.

---

### **3. Executar o Pipeline**

1. Volte para a página inicial do Jenkins e clique na pipeline recém-criada.
2. Clique em **"Construir Agora"** para iniciar o pipeline.
3. Monitore a execução:
   - Acompanhe os logs para verificar se os containers Docker (Prometheus, Grafana) foram provisionados corretamente.
   - Certifique-se de que a etapa final indica que o serviço Grafana está em execução.

    **Tela da Pipeline:**
   ![alt text](image-3.png)

---

### **4. Rodar o Projeto Manualmente (Sem o Jenkins)**

Caso não deseje utilizar o Jenkins para rodar o projeto, é possível executá-lo diretamente com o Docker Compose. Para isso, siga os passos abaixo:

1. Navegue até o diretório do projeto no terminal.  
2. Execute o comando:  

   ```bash
   docker compose up --build -d
   ```

3. Após a execução, acesse as aplicações nos seguintes endereços:  
   - **Aplicação**: [http://localhost:5000](http://localhost:5000)  
   - **Grafana**: [http://localhost:3000](http://localhost:3000)

---

### **5. Acessar o Grafana**

1. Abra o navegador e vá para `http://localhost:3000`.
2. Faça login no Grafana:
   - **Usuário**: `admin`  
   - **Senha**: `admin` (ou a configurada no ambiente).
3. Verifique o dashboard provisionado automaticamente e visualize as métricas de requisições.

   **Dashboard que você verá no Grafana:**
   ![alt text](img3-trabdevops)

   **Observação**: O carregamento dos gráficos do dashboard pode demorar aproximadamente **30 segundos** após acessar a aplicação (Também recomendo configurar o **time range** do dashboard em `last 5 minutes`).

---

## **Resumo dos Passos**

1. Certifique-se de que o Jenkins está rodando (ou opte por rodar diretamente via Docker Compose).  
2. Crie uma nova pipeline no Jenkins seguindo as instruções acima.  
3. Execute a pipeline ou o comando `docker compose up --build -d`.  
4. Acesse a aplicação Flask em `http://localhost:3000`, o Grafana em `http://localhost:3000` e explore o dashboard.  

---
