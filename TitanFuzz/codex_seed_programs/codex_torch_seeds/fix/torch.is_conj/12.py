'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_conj\ntorch.is_conj(input)\n'
import torch
input_data = torch.rand(2, 3)
print('Input data: ', input_data)
print('Is conjugate: ', torch.is_conj(input_data))