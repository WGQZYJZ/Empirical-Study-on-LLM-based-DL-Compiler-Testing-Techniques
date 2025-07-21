'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.cholesky\ntorch.linalg.cholesky(A, *, upper=False, out=None)\n'
import torch
A = torch.tensor([[4, 12, (- 16)], [12, 37, (- 43)], [(- 16), (- 43), 98]], dtype=torch.float32)
L = torch.linalg.cholesky(A)
print(L)