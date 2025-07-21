'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.symeig\ntorch.symeig(input, eigenvectors=False, upper=True, *, out=None)\n'
import torch
input = torch.rand(3, 3)
print('Input: \n{}'.format(input))
(eigenvalues, eigenvectors) = torch.symeig(input, eigenvectors=True, upper=True)
print('Eigenvalues: \n{}'.format(eigenvalues))
print('Eigenvectors: \n{}'.format(eigenvectors))