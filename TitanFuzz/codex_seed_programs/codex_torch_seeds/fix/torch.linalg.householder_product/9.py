'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.householder_product\ntorch.linalg.householder_product(A, tau, *, out=None)\n'
import torch
A = torch.randn(3, 3)
tau = torch.randn(3)
torch.linalg.householder_product(A, tau)
torch.linalg.householder_product(A, tau, out=A)