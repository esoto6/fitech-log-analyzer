from abc import ABC, abstractmethod
import pandas as pd

class FitechFileReader(ABC):
    def __init__(self, file_path, file_obj):
        self.file_path = file_path
        self.file_obj = file_obj
        self.sample_rate = 0.1

    @abstractmethod
    def read(self):
        """Read the file and return data as a dataframe"""
        pass


class BasicSensorReader(FitechFileReader):

    def read(self):
        df = pd.read_csv(self.file_obj)

        # Remove duplicate rows
        df = df[df['RPM'] != 'RPM']
        df = df.reset_index(drop=True)

        for col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

        df.drop(df.columns[df.columns.str.contains('Unnamed: 37', case=False)], axis=1, inplace=True)

        if 'Time' not in df.columns:
            df['Time'] = df.index * self.sample_rate
        
        return df
        
class DashboardReader(FitechFileReader):


    def read(self):

        df = pd.read_csv(self.file_obj)

        return df

def get_reader(file_path:str, file_obj) -> FitechFileReader:
    fileName = file_path.lower()

    if "basic sensor" in fileName:
        return BasicSensorReader(file_path, file_obj)
    elif "dashboard" in fileName:
        return DashboardReader(file_path, file_obj)
    else:
        raise ValueError(f"Unsupported log for Fitech: {file_path}")