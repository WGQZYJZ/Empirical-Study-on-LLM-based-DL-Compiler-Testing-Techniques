'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lu\ntorch.lu(A, pivot=True, get_infos=False, *, out=None)\n'
import torch
A = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(A)
(LU, pivots) = torch.lu(A)
print(LU)
print(pivots)
print(LU.matmul(LU.t()))