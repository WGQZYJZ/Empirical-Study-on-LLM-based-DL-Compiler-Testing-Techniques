'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.multi_dot\ntorch.linalg.multi_dot(tensors, *, out=None)\n'
import torch
a = torch.rand(3, 5)
b = torch.rand(5, 7)
c = torch.rand(7, 2)
torch.linalg.multi_dot([a, b, c])
torch.linalg.multi_dot([a, b, c], out=torch.zeros(3, 2))