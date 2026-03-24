class DataReader:

    @staticmethod
    def read_json(file):
        import json
        with open(file) as f:
            return json.load(f)

    @staticmethod
    def read_excel(file,sheet_name=0):
        import pandas as pd

        df = pd.read_excel(file,sheet_name=sheet_name)

        print("data",df)

        return df.to_dict(orient="records")