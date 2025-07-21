'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bmm\ntorch.bmm(input, mat2, *, deterministic=False, out=None)\n'
import torch
x = torch.randn(10, 3, 4)
y = torch.randn(10, 4, 5)
z = torch.bmm(x, y)
print(z)