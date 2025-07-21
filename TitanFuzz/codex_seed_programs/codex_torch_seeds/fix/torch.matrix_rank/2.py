'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.matrix_rank\ntorch.matrix_rank(input, tol=None, symmetric=False, *, out=None)\n'
import torch
input = torch.randn(3, 5, dtype=torch.float, requires_grad=True)
print('Input data: ', input)
rank = torch.matrix_rank(input)
print('Rank of the input data: ', rank)