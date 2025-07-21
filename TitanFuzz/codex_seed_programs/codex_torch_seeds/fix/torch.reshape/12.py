'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.reshape\ntorch.reshape(input, shape)\n'
import torch
input = torch.randn(1, 3, 3)
print('Input data:')
print(input)
print('Input data shape:')
print(input.shape)
output = torch.reshape(input, (1, 9))
print('Output data:')
print(output)
print('Output data shape:')
print(output.shape)