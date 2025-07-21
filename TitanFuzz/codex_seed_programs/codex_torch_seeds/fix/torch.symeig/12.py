'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.symeig\ntorch.symeig(input, eigenvectors=False, upper=True, *, out=None)\n'
import torch
A = torch.tensor([[1, 2, 3], [2, 4, 5], [3, 5, 6]], dtype=torch.float32)
(eigenvalues, eigenvectors) = torch.symeig(A, eigenvectors=True)
print(eigenvalues)
print(eigenvectors)
eigenvalues = torch.symeig(A, eigenvectors=False)
print(eigenvalues)