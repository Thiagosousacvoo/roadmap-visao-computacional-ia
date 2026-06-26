import logging
from src.utils import setup_logger, timer
from src.dataset import DataLoader
from src.processor import DataProcessor

@timer
def executar_pipeline():
    logging.info("--- Iniciando Pipeline ETL ---")
    
    # 1. Carregar (Instanciar DataLoader)
    
    # 2. Processar (Instanciar DataProcessor)
    
    # 3. Analisar
    
    logging.info("--- Pipeline Finalizado ---")

if __name__ == "__main__":
    setup_logger()
    executar_pipeline()
