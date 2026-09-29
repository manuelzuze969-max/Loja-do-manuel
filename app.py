from flask import Flask, render_template_string
app = Flask(__name__)
HTML = """
<!DOCTYPE html>
<html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width, initial-scale=1'>
<title>Loja do Manuel</title>
<style>body{font-family:Arial;margin:0;background:#f5f5f5}header{background:#075e54;color:white;padding:15px;text-align:center}.card{background:white;margin:15px;padding:15px;border-radius:10px}.btn{background:#25D366;color:white;padding:12px;border:none;border-radius:25px;width:100%;display:block;text-align:center;text-decoration:none}</style>
</head><body>
<header><h2>Loja do Manuel</h2><p>Matola - Entrega Rapida</p></header>
<div class='card'><h3>Produtos</h3><p><b>Arroz 25kg</b> - 1800 MT</p><p><b>Oleo 5L</b> - 650 MT</p><p><b>Acucar 10kg</b> - 900 MT</p><a class='btn' href='https://wa.me/258820000000'>Pedir no WhatsApp</a></div>
</body></html>
"""
@app.route('/')
def home(): return render_template_string(HTML)
if __name__ == '__main__': app.run()
