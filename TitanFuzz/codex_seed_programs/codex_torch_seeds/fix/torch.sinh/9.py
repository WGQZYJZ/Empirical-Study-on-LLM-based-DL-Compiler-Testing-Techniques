'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sinh\ntorch.sinh(input, *, out=None)\n'
import torch
x = torch.tensor([(- 1), 0, 1])
print(torch.sinh(x))