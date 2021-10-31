import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

function_selectBox = st.sidebar.selectbox("function", ("Draw graph", "Analysis"))


def selectFreqUnit(unit: str, freq: float):
    """
    选择频率单位
    :param unit: 单位
    :param freq: 频率值
    :return: 频率值*单位
    """
    if unit == "Hz":
        return freq * pow(10, 0)
    elif unit == "KHz":
        return freq * pow(10, 3)
    elif unit == "MHz":
        return freq * pow(10, 6)
    elif unit == "GHz":
        return freq * pow(10, 9)
    else:
        return freq


def selectMagUnit(unit: str, mag: float):
    """
    选择幅度单位
    :param unit: 单位
    :param mag: 幅度
    :return: 幅度*单位
    """
    if unit == "V":
        return mag * pow(10, 0)
    elif unit == "mV":
        return mag * pow(10, -3)
    elif unit == "μV":
        return mag * pow(10, -6)
    else:
        return mag


def drawSinWave(freq, mag):
    """
    画正弦图像
    :param freq: 频率
    :param mag: 幅度
    :return:
    """
    T = 1 / freq * 5  # 观测时间5个周期/s
    fs = 20 * freq;  # 采样频率
    d = 1 / fs
    t = np.arange(-T, T, d)  # X的范围位于【-3，3】
    w = 2 * np.pi * freq
    y = mag * np.sin(w * t)
    # 画图
    fig, ax = plt.subplots()
    ax.plot(t, y, ls='-', lw=2, label='幅度', color='g')
    st.title(r'$y=\sin(\pi\times x)$')  # 这是latex的表达式，与matlplotlib兼容
    return fig


if function_selectBox == 'Draw graph':
    row13_spacer1, row13_1, row13_spacer2, row13_2, row13_spacer3 = st.columns(
        (.2, 2.3, .2, 2.3, .2))
    with row13_1:
        freq = st.number_input('频率', None, None, 10.0)
        st.write('The current frequency is', freq)
    with row13_2:
        freqUnits = st.selectbox("Units", ["Hz", "KHz", "MHz", "GHz"])

    row14_spacer1, row14_1, row14_spacer2, row14_2, row14_spacer3 = st.columns(
        (.2, 2.3, .2, 2.3, .2))
    with row14_1:
        mag = st.number_input('幅度', None, None, 1.0)
        st.write('The current magnitude is', mag)
    with row14_2:
        magUnits = st.selectbox("Units", ["V", "mV", "μV"])
    real_freq = selectFreqUnit(freqUnits, freq)
    real_mag = selectMagUnit(magUnits, mag)
    fig = drawSinWave(real_freq, real_mag)
    st.pyplot(fig)


# progress_bar = st.sidebar.progress(0)
# status_text = st.sidebar.empty()
# last_rows = np.random.randn(1, 1)
# chart = st.line_chart(last_rows)
#
# for i in range(1, 101):
#     new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
#     status_text.text("%i%% Complete" % i)
#     chart.add_rows(new_rows)
#     progress_bar.progress(i)
#     last_rows = new_rows
#     time.sleep(0.05)
#
# progress_bar.empty()
#
# # Streamlit widgets automatically run the script from top to bottom. Since
# # this button is not connected to any other logic, it just causes a plain
# # rerun.
st.button("Re-run")
