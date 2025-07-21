'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arcsin\ntorch.arcsin(input, *, out=None)\n'
import torch
x = torch.tensor([(- 1), (- 0.5), 0, 0.5, 1])
y = torch.arcsin(x)
print(y)
y = torch.asin(x)
print(y)