import streamlit as st
import numpy as np
import joblib


st.title('Predição de Ocorrência de Incêndios Florestais')

st.subheader('Complete os dados abaixo e clique em Verificar')


diasemchuva=st.slider('Dias sem chuva', 0, 365)
precipitacao=st.slider('Precipitação', 0.0, 114.4)
frp=st.slider('FRP',0.0,6000.0)
lat=st.slider('Latitude',-9.5915,-3.12521)
lon=st.slider('Longitude',-55.477,-51.921)
temperatura=st.slider('Temperatura (Hora)',0.0,40.0)
umid=st.slider('Umidade(%)',0.0,100.0)
pressao=st.slider('Pressão (hPa)',0.0,1100.0)
vel_vento=st.slider('Velocidade do Vento(m/s)',0.0,10.0)
dir_vento=st.slider('Dir. Vento(m/s',0.0,360.0)
nebulosidade=st.slider('Nebulosidade',0.0,15.0)
insolacao=st.slider('Insolação(h)',0.0,12.0)
temp_max=st.slider('Temperatura Máxima',0.0,50.0)
temp_min=st.slider('Temperatura Mínima',0.0,50.0)
chuva=st.slider('Chuva(mm)',0.0,100.0)


teste = np.array([[diasemchuva,precipitacao,lat,lon,frp, temperatura,umid,pressao,vel_vento,dir_vento,nebulosidade,insolacao,temp_max,temp_min,chuva]])

model=joblib.load('Model/model2.joblib')

if st.button('Verificar'):

    prediction= model.predict(teste)[0]
    st.write(prediction)
    if prediction < 0.50:
        st.write("Baixo Risco de Incêndios")

    elif prediction < 0.80:
        st.write("Risco Moderado de Incêndios")

    else:
        st.write("Alto Risco de Incêndios")

else:
    st.write("clique em verificar para gerar a predição")