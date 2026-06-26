import pandas as pd
import logging

class DataLoader:
    """Classe responsável pelo Ingestão de dados."""
    def __init__(self, filepath: str):
        self.filepath = filepath
        self._df = None

    def carregar(self) -> pd.DataFrame:
        logging.info(f"Carregando dados de {self.filepath}")
        # TODO: Use pd.read_csv
        pass
