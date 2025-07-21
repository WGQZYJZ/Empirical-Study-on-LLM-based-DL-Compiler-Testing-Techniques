'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unsqueeze\ntorch.unsqueeze(input, dim)\n'
import torch
x = torch.randn(2, 3)
print(x)
print(x.size())
y = torch.unsqueeze(x, 0)
print(y)
print(y.size())
y = torch.unsqueeze(x, 1)
print(y)
print(y.size())
y = torch.unsqueeze(x, 2)
print(y)
print(y.size())