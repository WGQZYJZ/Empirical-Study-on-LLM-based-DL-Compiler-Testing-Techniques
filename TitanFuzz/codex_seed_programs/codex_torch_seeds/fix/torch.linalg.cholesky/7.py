'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.cholesky\ntorch.linalg.cholesky(A, *, upper=False, out=None)\n'
import torch
A = torch.Tensor([[4.0, (- 1.0), 1.0], [(- 1.0), 4.0, (- 1.0)], [1.0, (- 1.0), 4.0]])
L = torch.linalg.cholesky(A)
print('L=', L)