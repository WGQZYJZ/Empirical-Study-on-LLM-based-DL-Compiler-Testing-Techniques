'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.signbit\ntorch.signbit(input, *, out=None)\n'
import torch
input_data = torch.randn(5, 5)
signbit_data = torch.signbit(input_data)
print('Input data: ', input_data)
print('Signbit data: ', signbit_data)