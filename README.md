# PoC
## 準備
```bash
docker image build -t sample/test:latest .
```
```bash
docker container run -d -p 8000:8000 --name test -v ${PWD}/backend:/app sample/test:latest
```
## テスト
```bash
streamlit run viewer.py
```