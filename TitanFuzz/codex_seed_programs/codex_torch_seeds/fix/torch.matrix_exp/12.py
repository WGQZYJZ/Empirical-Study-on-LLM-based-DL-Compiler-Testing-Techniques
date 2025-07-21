'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.matrix_exp\ntorch.matrix_exp(input)\n'
import torch
n = 2
m = 2
A = torch.randn(n, m)
print(A)
B = torch.matrix_exp(A)
print(B)