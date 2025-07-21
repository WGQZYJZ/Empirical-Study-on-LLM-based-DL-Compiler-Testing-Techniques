'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.eig\ntorch.eig(input, eigenvectors=False, *, out=None)\n'
import torch
input_data = torch.randn(3, 3)
(eigenvalues, eigenvectors) = torch.eig(input_data, True)
print('\nEigenvalues: ', eigenvalues)
print('\nEigenvectors: ', eigenvectors)