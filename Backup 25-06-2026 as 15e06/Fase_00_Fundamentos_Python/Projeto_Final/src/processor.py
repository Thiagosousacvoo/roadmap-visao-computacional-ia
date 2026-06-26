import pandas as pd

class DataProcessor:
    """Aplica transformações pesadas e limpezas."""
    def __init__(self, df: pd.DataFrame):
        self.df = df
        
    def limpar_nulos(self):
        # TODO: Implementar lógica de limpeza
        pass
