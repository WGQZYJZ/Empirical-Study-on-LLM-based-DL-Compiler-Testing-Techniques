'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.squeeze\ntorch.squeeze(input, dim=None, *, out=None)\n'
import torch
x = torch.zeros(2, 1, 2, 1, 2)
print(x.size())
print(x)
y = torch.squeeze(x)
print(y.size())
z = torch.squeeze(x, 1)
print(z.size())
w = torch.squeeze(x, 0)
print(w.size())
u = torch.squeeze(x, 4)
print(u.size())