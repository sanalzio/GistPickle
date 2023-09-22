import os
import pickle
import base64
import pygistdb

class congist:
    def __init__(self, gistid: str, filename: str, token: str):
        self.gistid=gistid
        self.filename=filename
        self.token=token
        gist = pygistdb.congist(self.gistid, self.filename, self.token)
        self.db = pygistdb.pydb(gist)

    def save_var(self, varid, data):
        # Önce belirtilen id'ye sahip bir değişkenin zaten kayıtlı olup olmadığını kontrol edelim
        if self.db.control(varid):
            raise Exception(
                "Already, a variable with this varID has been previously saved."
            )

        # Veriyi pickle ile dosyaya kaydedip base64 ile kodlayalım
        with open(f"{varid}.pkl", "wb") as file:
            pickle.dump(data, file)

        with open(f"{varid}.pkl", "rb") as file:
            encoded_data = base64.b64encode(file.read()).decode()

        # Veriyi Gist'e yükleyelim
        self.db.addData(varid, encoded_data)

        # Dosyayı silelim
        os.remove(f"{varid}.pkl")

    def set_var(self, varid, data):
        # Veriyi pickle ile dosyaya kaydedip base64 ile kodlayalım
        with open(f"{varid}.pkl", "wb") as file:
            pickle.dump(data, file)

        with open(f"{varid}.pkl", "rb") as file:
            encoded_data = base64.b64encode(file.read()).decode()

        # Veriyi Gist'e yükleyelim
        self.db.setData(varid, encoded_data)

        # Dosyayı silelim
        os.remove(f"{varid}.pkl")

    def get_var(self, varid):
        # Gist'ten veriyi alalım
        encoded_data = self.db.getData(varid)

        if encoded_data != None:
            # Base64 ile kodlanmış veriyi çözüp pickle dosyasına kaydedelim
            with open(f"{varid}.pkl", "wb") as file:
                file.write(base64.b64decode(encoded_data.encode()))

            # Pickle dosyasını okuyarak veriyi alalım
            with open(f"{varid}.pkl", "rb") as file:
                data = pickle.load(file)

            # Dosyayı silelim
            os.remove(f"{varid}.pkl")

            return data
        else:
            return None
    
    def del_var(self, key):
        self.db.removeData(key)