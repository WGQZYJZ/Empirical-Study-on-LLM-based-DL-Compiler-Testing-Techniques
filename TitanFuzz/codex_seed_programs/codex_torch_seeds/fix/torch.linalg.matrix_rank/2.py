'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.matrix_rank\ntorch.linalg.matrix_rank(A, tol=None, hermitian=False, *, out=None)\n'
import torch
A = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float32)
r = torch.linalg.matrix_rank(A)
print('Rank of matrix A is: {}'.format(r))