'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.matrix_rank\ntorch.linalg.matrix_rank(A, tol=None, hermitian=False, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
print('Input data: ', input_data)
rank = torch.linalg.matrix_rank(input_data)
print('Rank of input data: ', rank)