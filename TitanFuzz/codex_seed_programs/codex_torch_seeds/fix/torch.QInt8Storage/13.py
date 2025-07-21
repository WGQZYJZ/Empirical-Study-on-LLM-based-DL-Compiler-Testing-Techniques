'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.QInt8Storage\ntorch.QInt8Storage(*args, **kwargs)\n'
import torch
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data_qint8 = torch.QInt8Storage(data)
print('data_qint8 = ', data_qint8)