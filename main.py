from flask import Flask, render_template, request
import matrix
import determinant

app = Flask(__name__)

def parse_value(val):
    if not val or str(val).strip() == '':
        return 0
    clean_val = str(val).replace(' ', '').replace('i', 'j')
    try:
        c = complex(clean_val)
        if c.imag == 0:
            return int(c.real) if c.real.is_integer() else c.real
        return c
    except ValueError:
        # Instead of returning 0, this explicitly triggers an error message
        raise ValueError(f"'{val}' is not a valid number. Please retry.")

def format_matrix(mat):
    if not mat:
        return None
    return [[str(val).strip('()').replace('j', 'i') for val in row] for row in mat]

def process_result(res):
    if res is None:
        return None
        
    def format_val(val):
        if isinstance(val, complex):
            return str(val).strip('()').replace('j', 'i')
        if isinstance(val, float) and val.is_integer():
            return str(int(val))
        return str(val)

    if isinstance(res, list):
        return [[format_val(item) for item in row] for row in res]
    return format_val(res)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    m1 = None
    m2 = None
    operation = '1'
    order = 2

    if request.method == 'POST':
        operation = request.form.get('operation')
        order = int(request.form.get('order'))
        
        try:
            def get_matrix(prefix):
                mat = []
                for i in range(order):
                    row = []
                    for j in range(order):
                        raw_val = request.form.get(f'{prefix}_{i}_{j}', '0')
                        row.append(parse_value(raw_val))
                    mat.append(row)
                return mat

            m1 = get_matrix('m1')
            
            if operation in ['1', '2', '3']:
                m2 = get_matrix('m2')
                if operation == '1':
                    result = matrix.addition(m1, m2, [])
                elif operation == '2':
                    result = matrix.subtraction(m1, m2, [])
                elif operation == '3':
                    result = matrix.multiply(m1, m2, [])
            elif operation == '4':
                result = matrix.square(m1, [])
            elif operation == '5':
                if order == 2:
                    result = determinant.orderTwo(m1)
                else:
                    result = determinant.orderThree(m1)
                    
        except Exception as e:
            # The raised ValueError gets caught here and sent to the HTML
            result = f"Input Error: {str(e)}"
            
    return render_template('index.html', 
                           result=process_result(result), 
                           m1=format_matrix(m1), 
                           m2=format_matrix(m2), 
                           operation=operation, order=order)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)