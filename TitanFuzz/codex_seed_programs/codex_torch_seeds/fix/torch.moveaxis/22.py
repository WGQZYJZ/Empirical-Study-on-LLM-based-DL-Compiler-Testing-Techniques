'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.moveaxis\ntorch.moveaxis(input, source, destination)\n'
import torch
input = torch.randn(3, 4, 5)
print('Input: \n', input)
print('Input shape: ', input.shape)
output = torch.moveaxis(input, 0, 2)
print('Output: \n', output)
print('Output shape: ', output.shape)
print('\n')
input = torch.randn(3, 4, 5)
print('Input: \n', input)
print('Input shape: ', input.shape)
output = torch.moveaxis(input, 1, 2)
print('Output: \n', output)
print('Output shape: ', output.shape)
print('\n')
input = torch.randn(3, 4, 5)
print('Input: \n', input)
print('Input shape: ', input.shape)
output = torch.moveaxis(input, 2, 1)
print('Output: \n', output)
print('Output shape: ', output.shape)