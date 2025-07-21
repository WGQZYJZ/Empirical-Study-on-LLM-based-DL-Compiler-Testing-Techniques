'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.symeig\ntorch.symeig(input, eigenvectors=False, upper=True, *, out=None)\n'
import torch
input = torch.randn(3, 3)
input = (input + input.t())
print(input)
(e_val, e_vec) = torch.symeig(input, eigenvectors=True, upper=False)
print(e_val)
print(e_vec)
e_val = torch.symeig(input, eigenvectors=False, upper=False)
print(e_val)