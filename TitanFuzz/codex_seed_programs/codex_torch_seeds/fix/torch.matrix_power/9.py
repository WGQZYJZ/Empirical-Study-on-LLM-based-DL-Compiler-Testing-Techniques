'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.matrix_power\ntorch.matrix_power(input, n, *, out=None)\n'
import torch
x = torch.rand(2, 2)
print(torch.matrix_power(x, 2))