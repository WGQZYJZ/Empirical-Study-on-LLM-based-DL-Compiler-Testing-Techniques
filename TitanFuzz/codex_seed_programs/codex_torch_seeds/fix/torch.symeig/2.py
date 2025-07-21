'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.symeig\ntorch.symeig(input, eigenvectors=False, upper=True, *, out=None)\n'
import torch
input = torch.randn(3, 3)
print('input = ', input)
(eig_value, eig_vector) = torch.symeig(input, eigenvectors=True)
print('eig_value = ', eig_value)
print('eig_vector = ', eig_vector)