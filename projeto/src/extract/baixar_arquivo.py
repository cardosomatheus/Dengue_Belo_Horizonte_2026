from pysus.ftp.databases.sinan import SINAN
from pysus.online_data.SINAN import metadata_df
import pandas as pd
from pathlib import Path

class DengueBeloHorizonte:
    sinan = SINAN().load()
 
    def __init__(self):
        # Resolve o diretório raiz automaticamente a partir da localização deste arquivo
        self.base_dir = Path(__file__).resolve().parent.parent.parent
        self.caminho_raw = self.base_dir / 'data' / 'raw'
        self.arquivo_bh_json = self.caminho_raw / 'dengue_bh.json'

    def download_dengue_json(self, year: int = 2026) -> None:
        """
        obs: 
            - Extração de dados da dengue focado no município de Belo Horizonte,
              O arquivo é extraido do DATASUS via biblioteca PySUS (SINAN) e salvo em formato json.
            - O arquivo é salvo em data/raw/dengue_bh.json.

        :param year: Inteiro com ano da extração
        """
        codigo_belo_horizonte = '310620'

        if not isinstance(year, int):
            raise Exception('o parâmetro ano deve ser um Inteiro: ex: year=2026')

        dataframe = self.sinan.download(
            self.sinan.get_files('DENG', year),
            local_dir=str(self.caminho_raw)
        ).to_dataframe()

        dataframe = dataframe[dataframe['ID_MUNICIP'] == codigo_belo_horizonte]
        print(f'✅ Exportando {len(dataframe)} registros para {self.arquivo_bh_json}...')
        dataframe.to_json(self.arquivo_bh_json, orient='records')

if __name__ == '__main__':
    dengue_extractor = DengueBeloHorizonte()
    dengue_extractor.download_dengue_json(2026)
