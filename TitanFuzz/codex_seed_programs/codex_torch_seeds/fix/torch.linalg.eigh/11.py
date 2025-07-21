"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eigh\ntorch.linalg.eigh(A, UPLO='L', *, out=None)\n"
import torch
A = torch.randn(3, 3)
A = (A @ A.t())
(eigenvalues, eigenvectors) = torch.linalg.eigh(A)
print('The eigenvalues are: {}'.format(eigenvalues))
print('The eigenvectors are: {}'.format(eigenvectors))
'\nThe eigenvalues are: tensor([-1.6148, -0.0363,  4.7409])\nThe eigenvectors are: tensor([[-0.8175, -0.5642,  0.1170],\n                              [-0.5642,  0.8175,  0.0942],\n                              [-0.1170, -0.0942,  0.9889]])\n'