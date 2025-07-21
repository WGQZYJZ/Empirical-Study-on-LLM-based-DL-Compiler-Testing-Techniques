'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.expit\ntorch.special.expit(input, *, out=None)\n'
import torch
x = torch.randn(1, 5)
print(x)
print(torch.sigmoid(x))
print(torch.special.expit(x))