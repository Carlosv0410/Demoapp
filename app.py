import streamlit as st 
st.title("demo")
st.sidebar.title("Parametros")
modulo=st.sidebar.selectbox("seleccione un modulo",["modulo1", "modulo2", "modulo3"])
if modulo == 'modulo1':
    st.write('usted esta en el modulo 1')
    GE = st.number_input("Ingrese la gravedad especifica", min_value = 0.1, max_value = 1.0, value = 0.83)
    api = (141.5/GE) - 131.5
    st.write("el valor api es: ", api)
elif modulo == 'modulo2':
    st.write('usted esta en el modulo 2')
else:
    st.write('usted esta en el modulo 3')
