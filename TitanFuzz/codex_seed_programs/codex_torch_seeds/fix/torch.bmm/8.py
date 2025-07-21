'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bmm\ntorch.bmm(input, mat2, *, deterministic=False, out=None)\n'
import torch
a = torch.rand(2, 3, 4)
b = torch.rand(2, 4, 5)
print(torch.bmm(a, b).size())
print(torch.bmm(a, b))