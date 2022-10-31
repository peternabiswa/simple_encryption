###simple_encryption

While working with a dataset that contained personal financial data, I thought it would be a good idea to create a simple
data anonymization program that could anonymise the data, instead of using an existing library function such as anonympy.
Program reads the Name column from a pdf file, and encrypts the names using a randomly generated anonymization code,
the encrypted names are then added back to the dataframe and saved as excel file.
The code used for encryption is also saved in a txt file and this can be used to convert the names back to their original form.

