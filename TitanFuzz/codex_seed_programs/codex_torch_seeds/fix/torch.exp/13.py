'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.exp\ntorch.exp(input, *, out=None)\n'
import torch
x = torch.tensor([1.0, 2.0, 3.0, 4.0])
y = torch.exp(x)
print(y)