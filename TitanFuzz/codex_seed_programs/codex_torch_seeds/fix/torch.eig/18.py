'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.eig\ntorch.eig(input, eigenvectors=False, *, out=None)\n'
import torch
a = torch.Tensor([[1, 2], [3, 4]])
(eigenvalues, eigenvectors) = torch.eig(a, True)
print('Eigenvalues: ', eigenvalues)
print('Eigenvectors: ', eigenvectors)