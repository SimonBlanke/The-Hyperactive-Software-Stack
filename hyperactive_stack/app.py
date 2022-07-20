import os
import sys
import gradient_free_optimizers
import streamlit as st

here_ = os.path.dirname(os.path.realpath(__file__))


st.set_page_config(page_title="The Hyperactive software stack", layout="wide")

st.markdown(
    """
        <style>
               .css-18e3th9 {
                    padding-top: 3rem;
                    padding-bottom: 5rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
               .css-1d391kg {
                    padding-top: 3rem;
                    padding-right: 3rem;
                    padding-bottom: 3rem;
                    padding-left: 3rem;
                }
        </style>
        """,
    unsafe_allow_html=True,
)


gfo_code = """
import numpy as np
from gradient_free_optimizers import RandomSearchOptimizer

def parabola_function(para):
    loss = para["x"] * para["x"]
    return -loss

search_space = {"x": np.arange(-10, 10, 0.1)}

opt = RandomSearchOptimizer(search_space)
opt.search(parabola_function, n_iter=100000)
"""

progress_board_code = """
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.datasets import fetch_california_housing

from hyperactive import Hyperactive
from hyperactive_progress_board import ProgressBoard # import progress board

data = fetch_california_housing()
X, y = data.data, data.target

progress = ProgressBoard() # init progress board


@progress.update # add decorator
def dtr_model(opt):
    dtr = DecisionTreeRegressor(
        min_samples_split=opt["min_samples_split"],
    )
    scores = cross_val_score(dtr, X, y, cv=5)
    return scores.mean()

search_space = {
    "max_depth": list(range(2, 50)),
    "min_samples_split": list(range(2, 50)),
    "min_samples_leaf": list(range(1, 50)),
}

progress.open() # open progress board before run begins

hyper = Hyperactive()
hyper.add_search(dtr_model, search_space, n_iter=1000)
hyper.run()
"""


hyperactive_url = "https://github.com/SimonBlanke/Hyperactive"
gfo_url = "https://github.com/SimonBlanke/Gradient-Free-Optimizers"
progress_board_url = "https://github.com/SimonBlanke/ProgressBoard"
surfaces_url = "https://github.com/SimonBlanke/Surfaces"
tde_url = "https://github.com/SimonBlanke/tabular-data-explorer"
data_collector = "https://github.com/SimonBlanke/simple-data-collector"


hyperactive_d = {
    "Gradient-Free-Optimizers": {
        "intro": "Backend of Hyperactive",
        "url": gfo_url,
        "code": gfo_code,
    },
    "Progress-Board": {
        "intro": "live visualization of optimization run",
        "url": progress_board_url,
        "code": progress_board_code,
    },
    "Surfaces": {
        "intro": "stuff",
        "url": surfaces_url,
        "code": gfo_code,
    },
    "Tabular-Data-Explorer": {
        "intro": "stuff",
        "url": tde_url,
        "code": gfo_code,
    },
    "Simple-Data-Collector": {
        "intro": "stuff",
        "url": data_collector,
        "code": gfo_code,
    },
}

gradient_free_optimizers_d = {
    "Hyperactive": {
        "intro": "stuff",
        "url": hyperactive_url,
        "code": gfo_code,
    },
    "Tabular-Data-Explorer": {
        "intro": "stuff",
        "url": tde_url,
        "code": gfo_code,
    },
    "Surfaces": {
        "intro": "stuff",
        "url": surfaces_url,
        "code": gfo_code,
    },
    "Simple-Data-Collector": {
        "intro": "stuff",
        "url": data_collector,
        "code": gfo_code,
    },
}

surfaces_d = {
    "Hyperactive": {
        "intro": "stuff",
        "url": hyperactive_url,
        "code": gfo_code,
    },
    "Gradient-Free-Optimizers": {
        "intro": "stuff",
        "url": gfo_url,
        "code": gfo_code,
    },
}

progress_board_d = {
    "Hyperactive": {
        "intro": "stuff",
        "url": hyperactive_url,
        "code": gfo_code,
    },
}

tabular_data_explorer_d = {
    "Hyperactive": {
        "intro": "stuff",
        "url": hyperactive_url,
        "code": gfo_code,
    },
    "Gradient-Free-Optimizers": {
        "intro": "stuff",
        "url": gfo_url,
        "code": gfo_code,
    },
}

simple_data_collector_d = {
    "Hyperactive": {
        "intro": "stuff",
        "url": hyperactive_url,
        "code": gfo_code,
    },
    "Gradient-Free-Optimizers": {
        "intro": "stuff",
        "url": gfo_url,
        "code": gfo_code,
    },
}


package_d = {
    "Hyperactive": hyperactive_d,
    "Gradient-Free-Optimizers": gradient_free_optimizers_d,
    "Surfaces": surfaces_d,
    "Progress-Board": progress_board_d,
    "Tabular-Data-Explorer": tabular_data_explorer_d,
    "Simple-Data-Collector": simple_data_collector_d,
}


choice_package = st.sidebar.radio("Package:", options=package_d, index=0)


for package_n in list(package_d[choice_package]):
    package_d_tmp = package_d[choice_package][package_n]
    # st.markdown("""## {0}""".format(package_n))
    st.header(package_n)

    st.components.v1.html(
        """<hr style="height:1px;border:none;color:#333;background-color:#333;" /> """,
        height=10,
    )

    col1, col2 = st.columns((1, 1))

    col1.write("")
    col1.write(package_d_tmp["intro"])
    col1.write("")
    col1.markdown("##### [Link to Repository](" + package_d_tmp["url"] + ")")

    col2.code(package_d_tmp["code"])

    for _ in range(5):
        st.write("")
