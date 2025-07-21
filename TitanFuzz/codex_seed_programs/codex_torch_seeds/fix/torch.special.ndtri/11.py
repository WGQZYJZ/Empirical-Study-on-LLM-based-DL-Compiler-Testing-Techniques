'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.ndtri\ntorch.special.ndtri(input, *, out=None)\n'
import torch
x = torch.randn(1, 3)
print('Input: ', x)
y = torch.special.ndtri(x)
print('Output: ', y)