'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.matrix_power\ntorch.matrix_power(input, n, *, out=None)\n'
import torch
input = torch.randn(2, 2)
print(input)
output = torch.matrix_power(input, 3)
print(output)