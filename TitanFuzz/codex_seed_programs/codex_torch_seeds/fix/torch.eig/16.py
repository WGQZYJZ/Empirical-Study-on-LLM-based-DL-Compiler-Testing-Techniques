'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.eig\ntorch.eig(input, eigenvectors=False, *, out=None)\n'
import torch
input = torch.randn(3, 3)
print('input: ', input)
(eig_val, eig_vec) = torch.eig(input, True)
print('eig_val: ', eig_val)
print('eig_vec: ', eig_vec)
eig_val = torch.eig(input, False)
print('eig_val: ', eig_val)