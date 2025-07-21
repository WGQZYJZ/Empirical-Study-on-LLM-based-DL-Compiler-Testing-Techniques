'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.svd\ntorch.linalg.svd(A, full_matrices=True, *, out=None)\n'
import torch
import torch
A = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
(U, S, V) = torch.linalg.svd(A)
print('U: ', U)
print('S: ', S)
print('V: ', V)