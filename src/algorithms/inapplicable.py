"""Module inapplicable.py"""
import numpy as np
import pandas as pd


class Inapplicable:
    """
    Addresses cases whereby a piece of text, in tokens form, does not have classifiable tokens.
    """

    def __init__(self):
        pass

    @staticmethod
    def exc(page: pd.DataFrame):
        """

        :param page:
        :return:
        """

        frame = page.copy()
        frame['code_of_tag_p'] = 0
        frame['tag_p'] = "O"
        frame['score'] = np.nan

        return frame
