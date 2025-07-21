'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.amin\ntorch.amin(input, dim, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(3, 4)
print('Input: \n', input)
print('\nMinimum element in each row: ', torch.amin(input, dim=1))
print('\nMinimum element in each column: ', torch.amin(input, dim=0))
print('\nMinimum element in the tensor: ', torch.amin(input))
print('\nMinimum element in each row with keepdim: ', torch.amin(input, dim=1, keepdim=True))
print('\nMinimum element in each column with keepdim: ', torch.amin(input, dim=0, keepdim=True))
print('\nMinimum element in the tensor with keepdim: ', torch.amin(input, keepdim=True))