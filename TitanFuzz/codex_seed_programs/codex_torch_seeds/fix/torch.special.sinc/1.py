'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.sinc\ntorch.special.sinc(input, *, out=None)\n'
import torch
x = torch.linspace((- 10), 10, steps=100)
y = torch.special.sinc(x)
print(x)
print(y)