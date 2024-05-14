from flask import Flask, request, jsonify
import pandas as pd
import io

app = Flask(__name__)

@app.route('/analise', methods=['GET', 'POST'])
def analisecotacao():
    productname = request.form['productname']
    file = request.files['file']

    df = pd.read_csv(io.StringIO(file.stream.read().decode("UTF8")), sep=',')
    df['actual_price'] = df['actual_price'].str.replace(r'[^\d.]', '', regex=True)
    df['actual_price'] = df['actual_price'].astype(float)
    df['actual_price'] = df['actual_price'] * 0.064
    df['actual_price'] = df['actual_price'].apply(lambda x: '{:,.2f}'.format(x).replace('.', ',').replace(',', '.', 1))
    produtos_filtrados = df[df['name'].str.contains(productname, case=False)]
    if not produtos_filtrados.empty:
        produtos_filtrados['actual_price'] = produtos_filtrados['actual_price'].str.replace('R$', '').str.replace('.', '').str.replace(',', '.').astype(float)
        produtos_filtrados = produtos_filtrados.sort_values(by='actual_price')
        top_produtos = produtos_filtrados.head(1)
        result = []
        for index, produto in top_produtos.iterrows():
            result.append({
                'Produto': produto['name'],
                'Preço': f"R$ {produto['actual_price']:.2f}",
                'Imagem': produto['image']
            })
        return jsonify(result)
    else:
        return jsonify({"message": "Nenhum produto encontrado com este nome no arquivo anexado."})

if __name__ == '__main__':
    app.run(debug=True)
