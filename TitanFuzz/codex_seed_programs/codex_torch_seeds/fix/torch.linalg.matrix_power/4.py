'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.matrix_power\ntorch.linalg.matrix_power(A, n, *, out=None)\n'
import torch
input_data = torch.rand(3, 3)
print(torch.linalg.matrix_power(input_data, 2))