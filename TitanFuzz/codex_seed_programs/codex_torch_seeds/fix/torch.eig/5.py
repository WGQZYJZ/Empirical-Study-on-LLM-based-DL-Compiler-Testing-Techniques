'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.eig\ntorch.eig(input, eigenvectors=False, *, out=None)\n'
import torch
input = torch.randn(3, 3)
(eigenvalues, eigenvectors) = torch.eig(input, True)
print(f'eigenvalues: {eigenvalues}')
print(f'eigenvectors: {eigenvectors}')