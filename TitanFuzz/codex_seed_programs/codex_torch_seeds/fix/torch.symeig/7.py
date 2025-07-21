'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.symeig\ntorch.symeig(input, eigenvectors=False, upper=True, *, out=None)\n'
import torch
input = torch.randn(3, 3)
(eigen_values, eigen_vectors) = torch.symeig(input, eigenvectors=True)
print(eigen_values)
print(eigen_vectors)