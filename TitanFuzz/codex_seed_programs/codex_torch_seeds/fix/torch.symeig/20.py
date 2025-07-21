'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.symeig\ntorch.symeig(input, eigenvectors=False, upper=True, *, out=None)\n'
import torch
input = torch.randn(10, 10)
input = input.mm(input.transpose(0, 1))
(eigenvalues, eigenvectors) = torch.symeig(input, eigenvectors=True)
print(eigenvalues)
print(eigenvectors)