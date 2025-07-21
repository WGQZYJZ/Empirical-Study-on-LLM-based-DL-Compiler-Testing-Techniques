'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.real\ntorch.real(input)\n'
import torch
x = torch.randn(4, 4)
print('Input: ', x)
y = torch.real(x)
print('Output: ', y)