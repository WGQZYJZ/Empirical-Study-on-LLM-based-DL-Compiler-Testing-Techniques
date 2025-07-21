'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.cholesky_ex\ntorch.linalg.cholesky_ex(A, *, upper=False, check_errors=False, out=None)\n'
import torch
A = torch.tensor([[4.0, 12.0, (- 16.0)], [12.0, 37.0, (- 43.0)], [(- 16.0), (- 43.0), 98.0]])
print('A = \n', A)
print('\nThe Cholesky decomposition of A is: ')
print('\nU = \n', torch.linalg.cholesky_ex(A, upper=False))
print('\nL = \n', torch.linalg.cholesky_ex(A, upper=True))