'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tanh\ntorch.tanh(input, *, out=None)\n'
import torch
x = torch.randn(2, 3)
print('Input:')
print(x)
y = torch.tanh(x)
print('Output:')
print(y)