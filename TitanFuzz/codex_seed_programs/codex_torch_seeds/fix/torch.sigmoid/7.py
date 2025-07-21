'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sigmoid\ntorch.sigmoid(input, *, out=None)\n'
import torch
x = torch.tensor([1.0, 2.0, 3.0])
y = torch.sigmoid(x)
print(y)
y = torch.sigmoid(torch.tensor([1, 2, 3]))
print(y)