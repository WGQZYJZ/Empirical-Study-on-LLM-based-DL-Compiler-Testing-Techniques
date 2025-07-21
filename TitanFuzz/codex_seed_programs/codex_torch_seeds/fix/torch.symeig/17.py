'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.symeig\ntorch.symeig(input, eigenvectors=False, upper=True, *, out=None)\n'
import torch
import torch
A = torch.tensor([[1.0, (- 1.0), 0.0], [(- 1.0), 1.0, 0.0], [0.0, 0.0, 2.0]])
(eigenvalues, eigenvectors) = torch.symeig(A, eigenvectors=True)
print('The eigenvalues of A are:', eigenvalues)
print('The eigenvectors of A are:', eigenvectors)