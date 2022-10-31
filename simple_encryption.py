
import string
import random
import re
import pandas as pd
import tabula
import json



def generator():
    # letters = string.ascii_lowercase
    characters = list(map(chr, range(50, 100)))
    x = 0
    values = []
    ch = ""
    while x < 26:
        for i in range(3):
             ch = ch + random.choice(characters)
        values.append(ch)
        x = x+1
        ch = ""

    return values


def get_key(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key
 
    return "key doesn't exist"

# Outputs the decoded message
def decode(encoded_message, decryption_key):
    words = encoded_message.split('#') # words = [one, two, three, four]
    dec_msg = ""
    codes = []


    for word in words:
        codes.extend(re.findall('...',word)) # ky = [xtz, wwe, we2, 23r]
        codes.append("###")
        

    for code in codes:
        if code == "###":
            dec_msg = dec_msg + " "
        else:
            dec_msg = dec_msg + get_key(code, decryption_key)
    
    return dec_msg
    


    # Takes a message and returns the encoded message based on the
def encode(message, encryption_code):
    enc_msg = ""
    for char in message:
        if char == " " or char == "-":
            enc_msg = enc_msg + "#" # is used as Place holder
        else:
            enc_msg = enc_msg + encryption_code[char]

    return enc_msg
     


def read_data(encryption_code):
        encoded_names = []
        file_path = "./Sales.pdf"
        encrypted_file = "Encoded_statement.xlsx"
        # pd.pandas.set_option('display.max_columns', None) - Shows all columns in the dataframe


        # create a dataframe from a pdf file using tabula
        df = tabula.read_pdf(file_path, pages='all')
        dfp = pd.DataFrame(df[0])
        dfp.columns = ['Full_name', 'ID', 'Product_id','Gender', 'Age', 'Units', 'price', 'total']

        names = dfp['Full_name'].values.tolist()
        
        # Convert the names to encrypted names
        for name in names:
            encoded_names.append(encode(name.lower(), encryption_code))

        # Replace the real names with encoded names in the dataframe
        dfp.drop('Full_name', axis=1, inplace=True)
        dfp.insert(0, 'Encoded_name', encoded_names)
      
        # create an excel file with encrypted names
        dfp.to_excel(encrypted_file, index=False)
        
        # create a text file with the encryption key
        with open('Encrytion_key.txt', 'w') as f:
            f.write(json.dumps(encryption_code))


def decode_file(encrypted_file_name, decryption_code):
        decoded_names = []
        decrypted_file = "Actual_statement.xlsx"
        # create a dataframe from a pdf file using tabula
        file_path = "./" + encrypted_file_name
        dfpr = pd.read_excel(file_path)
        dfpr.columns = ['Encoded_name', 'ID', 'Product_id','Gender', 'Age', 'Units', 'price', 'total']

        names = dfpr['Encoded_name'].values.tolist()
        
        # Convert the names to encrypted names
        for name in names:
            decoded_names.append(decode(name, decryption_code))

        # Replace the real names with encoded names in the dataframe
        dfpr.drop('Encoded_name', axis=1, inplace=True)
        dfpr.insert(0, 'Full_name', decoded_names)
      
        # create an excel file with encrypted names
        dfpr.to_excel(decrypted_file, index=False)



    # Takes in a list of names
    # Encrypts the list and returning a new list of encrypted names and the encryption key. 
    # Result => Ecrypted_list, Encryption_key

def main():
   encryption_code = dict(zip(string.ascii_lowercase, generator()))
   read_data(encryption_code)
   enc_file = "Encoded_statement.xlsx"
   decode_file(enc_file, encryption_code)
   

if __name__ == "__main__":
    main()