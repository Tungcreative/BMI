import streamlit as st

st.title('Welcome to BMI Caculator')
can_nang = st.number_input('Hãy điền cân nặng của bạn bằng đơn vị kg')
chieu_cao = st.number_input('Hãy điền chiều cao của bạn bằng đơn vị m')
if st.button('Calculate BMI'):
    bmi = can_nang / (chieu_cao * chieu_cao)
    st.balloons()
    st.image('BMI.png')
    st.subheader('Chỉ số BMI của bạn là: ' + str(bmi))

    if bmi <= 18.5:
        st.info('Nhẹ cân')
    if bmi >= 18.5 and bmi <= 24.9:
        st.success('Bình thường')
    if bmi >= 25 and bmi <= 29.9:
        st.warning('Thừa cân')
    if bmi >= 30 and bmi <= 34.9:
        st.error('Béo phì độ I')
    if bmi >= 35:
        st.exception(can_nang('Béo phì độ II trở lên'))