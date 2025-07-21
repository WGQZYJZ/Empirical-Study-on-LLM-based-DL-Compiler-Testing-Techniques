'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.householder_product\ntorch.linalg.householder_product(A, tau, *, out=None)\n'
import torch
A = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]], dtype=torch.float32)
tau = torch.tensor([1.0], dtype=torch.float32)
out = torch.linalg.householder_product(A, tau)
print('A = ', A)
print('tau = ', tau)
print('out = ', out)