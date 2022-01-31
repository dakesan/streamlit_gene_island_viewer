# %%
from dna_features_viewer import GraphicFeature, GraphicRecord

import streamlit as st

import matplotlib.colors as mcolors

color_pal = list(mcolors.TABLEAU_COLORS)*3

st.markdown('# 簡易DNAプロットアプリ')
st.markdown('by dakesan')

st.sidebar.title("Control Panel")
left_col, middle_col, right_col = st.columns(3)

st.sidebar.subheader("遺伝子数を選ぶ")
num_genes = st.sidebar.number_input(
    "Number of prior sessions",
    min_value=1,
    max_value=None,
    value=4,
    step=1
)



def make_num_query(in_text,in_key):
    var_input = st.sidebar.number_input(
    in_text,
    min_value=None,
    max_value=None,
    value=1000,
    step=1,
    key=in_key
    )
    return var_input


start_end_info = []
st.sidebar.subheader("遺伝子の始点・終点を入力")

for i in range(num_genes):
    in_text = 'Gene_'+str(i)+': start'
    in_key = 'start_keys'+str(i)
    result_start = make_num_query(in_text, in_key)
    in_text = 'Gene_'+str(i)+': end'
    in_key = 'end_keys'+str(i)
    result_end = make_num_query(in_text, in_key)
    start_end_info.append((result_start, result_end))

if st.sidebar.button('Generate plot!'):
    features=[]
    lens = []
    for index, start_end in enumerate(start_end_info):
        n_start, n_end = start_end
        strand=+1 if n_end - n_start > 0 else -1
        if n_end - n_start > 0:
            pass
        else:
            n_end, n_start = (n_start, n_end)
        features.append(
            GraphicFeature(start=n_start,
                            end=n_end,
                            strand=strand,
                            color=color_pal[index],
                            label='Gene_'+str(index)
        ))
        lens.append(n_end)
        
    max_len = max(lens)

    record = GraphicRecord(sequence_length = max_len+1000,
                            features=features)
    fig = record.plot_with_bokeh(figure_width=6)
        
    st.bokeh_chart(fig, use_container_width=True)
    
########################################################
    


# %%
