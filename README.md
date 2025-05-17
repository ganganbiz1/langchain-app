# langchain-app

## 概要
親しみやすいAIキャラクターと対話できるLangchainアプリケーションです。Ollama（llama3モデル）と連携し、Docker Composeで簡単に起動できます。

## セットアップ

1. DockerとDocker Composeをインストールしてください。
2. 以下のコマンドで起動します。

```
docker compose up --build
```

- 初回起動時はOllamaがllama3モデルを自動ダウンロードします。
- アプリは http://localhost:8000 でAPIサーバーが立ち上がります。

## APIの使い方

### 会話エンドポイント
- `POST /chat`
- リクエスト例:

```
curl -X POST http://localhost:8000/chat \
  -H 'Content-Type: application/json' \
  -d '{"message": "こんにちは！"}'
```

- レスポンス例:
```
{"response": "こんにちは！今日も元気ですか？"}
```