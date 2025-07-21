'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fmod\ntorch.fmod(input, other, *, out=None)\n'
import torch
input_data = torch.randn(3, 3)
print('Input data: ', input_data)
modulus_data = torch.fmod(input_data, 2)
print('Modulus data: ', modulus_data)