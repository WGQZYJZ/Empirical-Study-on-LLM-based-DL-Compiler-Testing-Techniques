'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.symeig\ntorch.symeig(input, eigenvectors=False, upper=True, *, out=None)\n'
import torch
A = torch.Tensor([[1, 2, 3], [2, 4, 5], [3, 5, 6]])
(eigen_values, eigen_vectors) = torch.symeig(A, eigenvectors=True)
print(eigen_values)
print(eigen_vectors)