'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.moveaxis\ntorch.moveaxis(input, source, destination)\n'
import torch
input = torch.rand(2, 3, 4)
print('Input:')
print(input)
print('\n')
output = torch.moveaxis(input, 0, 1)
print('Output:')
print(output)
print('\n')