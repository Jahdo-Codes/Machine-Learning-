import streamlit as st
import numpy as np

st.title('Matrix Calculator')

operation = st.selectbox("What option would you like to perform on your matrices?",
             ('Addition','Subtraction','Multiplication')
            )


st.subheader('Enter the matrix dimensions')
matrix_a_str = st.text_area("Enter matrix A (Separate rows by new line & numbers by spaces)", "1 2 \n3 4")

matrix_b_str = st.text_area("Enter matrix B (Separate rows by new line & numbers by spaces)", "1 2 \n3 4")

def parse_matrix(matrix_str):
    try:
        return np.array([
            list(map(int, row.split()))
            for row in matrix_str.strip().split('\n')
        ])
    except:
        return None

A = parse_matrix(matrix_a_str)
B = parse_matrix(matrix_b_str)

if (A is None) or (B is None):
    st.error('Matrix A and Matrix B are not valid.Please check formatting')

elif st.button('Calculate'):
    st.write('Matrix A')
    st.write(A)
    st.write('Matrix B')
    st.write(B)

    try:
        if operation == 'Multiplication':
            if A.shape[1] != B.shape[0]: #Checks if col_A = col_B
                st.error('Matrix A and Matrix B dimensions are not compatible.')

            else:
                result = np.dot(A,B) #Performs matrix multiplication
                st.success(f"Result of A x B {result}")
                st.write(result)

        elif operation == 'Subtraction':
            if A.shape != B.shape: #Checks if matrix A and B have the same dimensions
                st.error('Matrix A and Matrix B dimensions are not compatible. [m x n != n x p]')

            else:
                result = A - B
                st.success(f"Result of A - B {result}")
                st.write(result)

        elif operation == 'Addition':
            if A.shape != B.shape: #Checks if matrix A and B have the same dimensions
                st.error('Matrix A and Matrix B dimensions are not compatible. [m x n != n x p]')

            else:
                result = A + B
                st.success(f"Result of A + B {result}")
                st.write(result)
        else:
            st.error('Invalid operation')


    except Exception as e:
        st.error(f'Calculation failed: {e}')





