'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.matrix_power\ntorch.matrix_power(input, n, *, out=None)\n'
import torch
a = torch.randn(3, 3)
print(a)
b = torch.matrix_power(a, 2)
print(b)
c = torch.matrix_power(a, 3)
print(c)