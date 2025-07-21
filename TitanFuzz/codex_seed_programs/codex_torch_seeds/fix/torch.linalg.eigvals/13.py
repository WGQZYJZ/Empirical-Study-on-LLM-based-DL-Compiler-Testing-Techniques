'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eigvals\ntorch.linalg.eigvals(A, *, out=None)\n'
import torch
A = torch.randn(4, 4)
eigenvalues = torch.linalg.eigvals(A)
print(eigenvalues)