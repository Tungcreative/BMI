import streamlit as st

st.title('Welcome to BMI Caculator')
can_nang = st.number_input('Hãy điền cân nặng của bạn bằng đơn vị kg')
tinh_toan = st.radio('Hãy chọn cân nặng của bạn qua:', ['xăng-ti-mét', 'đề-xi-mét', 'mét'])
chieu_cao = st.number_input('Hãy điền chiều cao của bạn')
if st.button('Caculate BMI'):
    calculate = can_nang / (chieu_cao * chieu_cao)
    st.subheader('Chỉ số BMI của bạn là: '+ str(calculate))
    if calculate <= 18.5:
        st.info('Nhẹ cân')
    if calculate >= 18.5 and calculate <= 24.9:
        st.success('Bình thường')
    if calculate >= 25 and calculate <= 30:
        st.warning('Thừa cân')
    if calculate >= 20 and calculate <= 34.9:
        st.error('Béo phì độ 1')
    if calculate >= 35:
        st.exception(can_nang('Béo phì độ 2 trở lên'))
st.image('BMI.png')