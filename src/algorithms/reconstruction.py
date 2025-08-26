
import pandas as pd

class Reconstruction:

    def __init__(self):

        self.__fields = ['word', 'tag_p', 'score', 'start', 'end']
        self.__rename = {'tag_p': 'entity'}

    def exc(self, mappings: pd.DataFrame):
        """

        :param mappings:
        :return:
        """


        frame = mappings.copy()[self.__fields]

        frame = frame.copy().loc[frame['score'].notna, :]
        frame.rename(columns=self.__rename, inplace=True)
