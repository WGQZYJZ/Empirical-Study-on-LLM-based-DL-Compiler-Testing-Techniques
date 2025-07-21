'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.conj\ntorch.conj(input)\n'
import torch
input_data = torch.rand(2, 2)
print('Input data is: ', input_data)
conj_data = torch.conj(input_data)
print('Conjugate data is: ', conj_data)