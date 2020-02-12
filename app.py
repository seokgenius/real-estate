import matplotlib.pyplot as plt
import pandas as pd
from flask import Flask
from flask import render_template

# 앱객체 생성
app = Flask(__name__)

# csv 데이터를 읽는다.
# dataset = tablib.Dataset()
# with open(os.path.join(os.path.dirname(__file__),'lease.csv')) as f:
#     dataset.csv = f.read()

@app.route('/')
def index():
    plt.rc('font', family='Malgun Gothic')
    plt.rc('font', size='10')

    df = pd.read_csv('pop_density_2018.csv')

    x = list(df.자치구)
    y = list(df.인구밀도)
    plt.title('구별 인구 밀도')
    plt.scatter(x, y, color='r')
    graph = plt.show()

    return render_template('index.html',
                           title = '구별 인구 밀도',
                           data = list(df.values.flatten()))

if __name__ == '__main__':
 app.run(debug=True)

# 앱 실행
# app.run(host='127.0.0.1', port=5000, debug=True)


