'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.symeig\ntorch.symeig(input, eigenvectors=False, upper=True, *, out=None)\n'
import torch
A = torch.rand(3, 3)
print(A)
(eigenvalues, eigenvectors) = torch.symeig(A, eigenvectors=True)
print(eigenvalues)
print(eigenvectors)