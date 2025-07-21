'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.symeig\ntorch.symeig(input, eigenvectors=False, upper=True, *, out=None)\n'
import torch
input = torch.randn(3, 3)
print('Input data: \n', input)
(eigenvalues, eigenvectors) = torch.symeig(input, eigenvectors=True)
print('Eigenvalues: \n', eigenvalues)
print('Eigenvectors: \n', eigenvectors)