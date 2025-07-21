'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.matrix_power\ntorch.matrix_power(input, n, *, out=None)\n'
import torch
A = torch.rand(3, 3)
print(A)
A_power_3 = torch.matrix_power(A, 3)
print(A_power_3)