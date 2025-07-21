'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.argmin\ntorch.argmin(input, dim=None, keepdim=False)\n'
import torch
import torch
input = torch.randn(3, 4)
print('Input: ', input)
output = torch.argmin(input, dim=1, keepdim=True)
print('Output: ', output)
print('Output shape: ', output.shape)
output = torch.argmin(input, dim=1, keepdim=False)
print('Output: ', output)
print('Output shape: ', output.shape)
output = torch.argmin(input, dim=0, keepdim=True)
print('Output: ', output)
print('Output shape: ', output.shape)
output = torch.argmin(input, dim=0, keepdim=False)
print('Output: ', output)
print('Output shape: ', output.shape)