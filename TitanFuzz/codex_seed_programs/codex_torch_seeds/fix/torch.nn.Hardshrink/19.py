'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardshrink\ntorch.nn.Hardshrink(lambd=0.5)\n'
import torch
x = torch.randn(3, 3)
hardshrink = torch.nn.Hardshrink(lambd=0.5)
y = hardshrink(x)
print('Input:')
print(x)
print('Output:')
print(y)