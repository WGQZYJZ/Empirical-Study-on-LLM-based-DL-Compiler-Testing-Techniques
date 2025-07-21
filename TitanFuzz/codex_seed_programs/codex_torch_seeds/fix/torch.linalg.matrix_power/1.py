'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.matrix_power\ntorch.linalg.matrix_power(A, n, *, out=None)\n'
import torch
import numpy as np
A = torch.tensor([[1, 2], [3, 4]])
print(A)
print(torch.linalg.matrix_power(A, 2))
print(torch.linalg.matrix_power(A, 3))
print(torch.linalg.matrix_power(A, 4))