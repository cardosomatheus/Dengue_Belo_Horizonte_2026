from src.transform.tratamentos import TratamentosDengue
import pandas as pd
from pathlib import Path

class SalvarArquivoCSV:
    tratamentos = TratamentosDengue()
    def __init__(self):
        self.base_dir = Path(__file__).resolve().parent.parent.parent
        self.arquivo_bh_tratado = self.base_dir / 'data' / 'processed' / 'dengue_bh_tratado.csv'

    def salva_arquivo_processado(self) -> None:
        """
            Salvando o arquivo tratado em um .csv na pasta data/processed/
            :return: None
        """
        dataframe = self.tratamentos.disponibiliza_dados_prontos_para_analise()
        dataframe.to_csv(self.arquivo_bh_tratado, sep=',', index=False, encoding='utf-8')
        print(f'✅ Arquivo salvo com sucesso em {self.arquivo_bh_tratado}')