from pathlib import Path
import pandas as pd
import pprint

class TratamentosDengue:
    def __init__(self):
        # Resolve o diretório raiz do projeto (onde a pasta 'data' está)
        self.base_dir = Path(__file__).resolve().parent.parent.parent
        self.arquivo_bh_json = self.base_dir / 'data' / 'raw' / 'dengue_bh.json'
        self.arquivo_bh_tratado = self.base_dir / 'data' / 'processed' / 'dengue_bh_tratado.csv'

    def disponibiliza_dados_prontos_para_analise(self) -> None:
        """
            Disponibiliza os dados prontos para analise
            :return: None
        """
        dataframe = self.lendo_arquivo_json()
        dataframe = self.padronizando_colunas(dataframe=dataframe)
        dataframe = self.mapeamento_dados(dataframe=dataframe)
        self.salva_arquivo_processado(dataframe=dataframe)


    def salva_arquivo_processado(self, dataframe: pd.DataFrame) -> None:
        """
            Salvando o arquivo tratado
            :param dataframe: DataFrame com os dados tratados
            :return: None
        """
        dataframe.to_csv(self.arquivo_bh_tratado, sep=',', index=False, encoding='utf-8')
        print(f'✅ Arquivo salvo com sucesso em {self.arquivo_bh_tratado}')


    def lendo_arquivo_json(self) -> pd.DataFrame:
        """
            Lendo o arquivo Json de Dengue extraido do site Pysus
            :return: DataFrame com os dados
        """
        try:
            df = pd.read_json(path_or_buf=self.arquivo_bh_json, orient='records', encoding='utf-8')
            print(f'✅ Tamanho do df: {len(df)} registros.')
            return df

        except Exception as e:
            print(f'❌ Erro ao ler o arquivo json: {e}')



    def padronizando_colunas(self, dataframe: pd.DataFrame):
        if not isinstance(dataframe, pd.DataFrame):
            raise Exception('O parâmetro passado em padronizacão não é um dataframe.')

        colunas_selecionadas = {
            'ANO_NASC': 'ano_nascimento',
            'HOSPITALIZ': 'ind_hospitalizacao',
            'CS_SEXO': 'sexo',
            'CS_GESTANT': 'id_estado_gestacional',
            'FEBRE': 'ind_febre',
            'MIALGIA': 'ind_mialgia',
            'CEFALEIA': 'ind_cefaleia',
            'EXANTEMA': 'ind_exantema',
            'VOMITO': 'ind_vomito',
            'NAUSEA': 'ind_nausea',
            'DOR_COSTAS': 'ind_dor_costas',
            'CONJUNTVIT': 'ind_conjuntivite',
            'ARTRITE': 'ind_artrite',
            'ARTRALGIA': 'ind_artralgia',
            'PETEQUIA_N': 'ind_petequia',
            'LEUCOPENIA': 'ind_leucopenia',
            'LACO': 'ind_prova_laco',
            'DOR_RETRO': 'ind_dor_retroorbital',
            'CLASSI_FIN': 'id_classificacao'
        }

        dataframe = dataframe[colunas_selecionadas.keys()]
        dataframe = dataframe.rename(columns=colunas_selecionadas)

        return dataframe    


    def mapeamento_dados(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """
            Mapeamento dos significados dos códigos de campos do DataFrame
            :param dataframe: DataFrame com os dados
            :return: DataFrame com os dados mapeados
        """
        if not isinstance(dataframe, pd.DataFrame):
            raise Exception('O parâmetro passado em mapeamento não é um dataframe.')

        mapeamento_dados = {
            'sexo': {
                'M': 'Masculino',
                'F': 'Feminino'
            },
            'id_estado_gestacional': {
                1: '1ºTrimestre',
                2: '2ºTrimestre',
                3: '3ºTrimestre',
                4: 'Idade gestacional Ignorada',
                5: 'Não',
                6: 'Não se aplica',
                9: 'Ignorado'
            },
            'id_classificacao': {
               '5': 'Descartado',
               '8': 'Em Investigação',
               '10': 'Dengue',
               '11': 'Dengue com Sinais de Alarme',
               '12': 'Dengue Grave',
               '13': 'Chikungunya',

            },
            'ind_hospitalizacao': {
                '1': 'Sim',
                '2': 'Não',
                '9': 'Ignorado',
                '': 'Não informado'
            }
        }

        dataframe['genero'] = dataframe['sexo'].map(mapeamento_dados['sexo']).fillna('Não informado')
        dataframe['estado_gestacional'] = dataframe['id_estado_gestacional'].map(mapeamento_dados['id_estado_gestacional']).fillna('Não informado')
        dataframe['classificacao_final'] = dataframe['id_classificacao'].map(mapeamento_dados['id_classificacao']).fillna('Não informado')
        dataframe['hospitalizacao'] = dataframe['ind_hospitalizacao'].map(mapeamento_dados['ind_hospitalizacao']).fillna('Não informado')
        return dataframe


if __name__ == '__main__':
    tratamentos = TratamentosDengue()
    dados = tratamentos.disponibiliza_dados_prontos_para_analise()    
    pprint.pprint(dados.head(2))
    pprint.pprint(dados['id_classificacao'].unique())
    #pprint.pprint(dados['id_estado_gestacional'].unique())
    #pprint.pprint(dados['id_classificacao_final'].unique())
    #pprint.pprint(dados['classificacao_final'].unique())
    #pprint.pprint(dados['sexo_literal'].unique())
    #pprint.pprint(dados['estado_gestacional'].unique())
    

