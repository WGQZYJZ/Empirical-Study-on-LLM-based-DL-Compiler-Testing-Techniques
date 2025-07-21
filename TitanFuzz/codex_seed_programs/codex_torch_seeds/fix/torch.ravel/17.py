'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ravel\ntorch.ravel(input)\n'
import torch
input_data = torch.randn(3, 3)
print('Input data: ')
print(input_data)
output = torch.ravel(input_data)
print('Output data: ')
print(output)