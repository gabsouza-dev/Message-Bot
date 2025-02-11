# 📩 WhatsApp & Telegram Bot Scheduler

Automação de envio de mensagens pelo WhatsApp (via Twilio) e Telegram, rodando no GitHub Actions.

## 🚀 Como funciona?

Este projeto permite enviar mensagens automaticamente pelo WhatsApp e Telegram em horários programados, utilizando **GitHub Actions** para a execução.

## 🛠 Tecnologias Utilizadas

- **Python 3.9+**
- **Twilio API** (para WhatsApp)
- **Telegram Bot API**
- **GitHub Actions** (para agendamento)

## ⚙️ Configuração

### 1️⃣ Obter Tokens e IDs

#### **🔹 WhatsApp (via Twilio)**
1. Crie uma conta em [Twilio](https://www.twilio.com/).
2. No painel do Twilio, obtenha:
   - `TWILIO_ACCOUNT_SID`
   - `TWILIO_AUTH_TOKEN`
   - Um número de telefone formatado como `whatsapp:+1415XXXXXXX`.
3. Ative a API do WhatsApp no Twilio e faça o teste de envio.

#### **🔹 Telegram**
1. No Telegram, abra o bot `@BotFather` e crie um novo bot com `/newbot`.
2. Copie o **TOKEN** gerado pelo BotFather (`TELEGRAM_BOT_TOKEN`).
3. Envie uma mensagem para o bot e obtenha o `CHAT_ID` através da URL:
   ```
   https://api.telegram.org/bot<TELEGRAM_BOT_TOKEN>/getUpdates
   ```
4. Pegue o `chat_id` da resposta JSON.

### 2️⃣ Configurar Secrets no GitHub

1. No GitHub, vá até **Settings** → **Secrets and variables** → **Actions**.
2. Adicione as seguintes variáveis:
   - `TWILIO_ACCOUNT_SID`
   - `TWILIO_AUTH_TOKEN`
   - `TELEGRAM_BOT_TOKEN`
   - `CHAT_ID`

### 3️⃣ Configurar GitHub Actions

O workflow do GitHub Actions está definido em `.github/workflows/bot-scheduler.yml` e já está pronto para rodar. Ele executa o bot automaticamente conforme o cron configurado.

## 📅 Agendamento (CRON)

O bot é executado diariamente às **14:00 UTC**. Para alterar o horário, edite o arquivo `bot-scheduler.yml` e modifique a linha:
```yaml
- cron: '0 14 * * *'  # Formato CRON: Minuto Hora Dia Mês DiaDaSemana
```
- Exemplo para rodar todo dia às 8h da manhã (UTC-3):
  ```yaml
  - cron: '0 11 * * *'  # 8h no Brasil (horário de Brasília)
  ```

## ▶️ Executando Manualmente

Além do agendamento, você pode rodar o bot manualmente pelo GitHub Actions:
1. Vá até a aba **Actions** do repositório.
2. Clique no workflow **WhatsApp/Telegram Bot Scheduler**.
3. Clique em **Run workflow**.

## 📜 Licença

Este projeto está sob a licença **MIT**. Sinta-se à vontade para modificar e melhorar! 💡

---

💬 Se tiver dúvidas ou sugestões, abra uma issue ou pull request! 🚀
