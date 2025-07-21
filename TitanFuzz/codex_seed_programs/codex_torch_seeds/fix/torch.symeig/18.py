'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.symeig\ntorch.symeig(input, eigenvectors=False, upper=True, *, out=None)\n'
import torch
A = torch.randn(3, 3)
A = A.mm(A.t())
(e, v) = torch.symeig(A, True)
print('Eigen Values: ', e)
print('Eigen Vectors: ', v)