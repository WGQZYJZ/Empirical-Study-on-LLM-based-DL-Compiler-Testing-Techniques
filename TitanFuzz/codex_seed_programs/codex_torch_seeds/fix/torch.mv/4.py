'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mv\ntorch.mv(input, vec, *, out=None)\n'
import torch
import torch
x = torch.rand(3, 4)
v = torch.rand(4)
y = torch.mv(x, v)
print(y)