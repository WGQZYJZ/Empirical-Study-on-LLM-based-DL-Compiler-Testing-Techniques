'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.triu\ntorch.triu(input, diagonal=0, *, out=None)\n'
import torch
x = torch.rand(5, 5)
print(x)
print(x.size())
print(x.shape)
y = torch.triu(x)
print(y)
print(y.size())
print(y.shape)
y1 = torch.triu(x, diagonal=1)
print(y1)
print(y1.size())
print(y1.shape)
y2 = torch.triu(x, diagonal=2)
print(y2)
print(y2.size())
print(y2.shape)