'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.cholesky_ex\ntorch.linalg.cholesky_ex(A, *, upper=False, check_errors=False, out=None)\n'
import torch
A = torch.tensor([[4, 12, (- 16)], [12, 37, (- 43)], [(- 16), (- 43), 98]], dtype=torch.float)
print('Input A: ', A)
L = torch.linalg.cholesky_ex(A, upper=False)
print('Cholesky decomposition: ', L)