'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eigvals\ntorch.linalg.eigvals(A, *, out=None)\n'
import torch
A = torch.randn((3, 3))
eigenvalues = torch.linalg.eigvals(A)
print('The eigenvalues of A are:', eigenvalues)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eigvalsh\ntorch.linalg.eigvalsh(A, *, out=None)\n'
import torch
A = torch.randn((3, 3))
eigenvalues = torch.linalg.eigvalsh(A)
print('The eigenvalues of A are:', eigenvalues)