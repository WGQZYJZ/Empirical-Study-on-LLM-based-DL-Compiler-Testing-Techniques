'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.matrix_power\ntorch.matrix_power(input, n, *, out=None)\n'
import torch
input = torch.randn(3, 3)
print(input)
print(torch.matrix_power(input, 3))
print(torch.pow(input, 3))
print((input ** 3))