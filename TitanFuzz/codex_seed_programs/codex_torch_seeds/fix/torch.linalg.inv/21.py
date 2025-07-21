'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.inv\ntorch.linalg.inv(A, *, out=None)\n'
import torch
A = torch.rand(5, 5)
print(A)
B = torch.rand(5, 5)
print(B)
inv_A = torch.linalg.inv(A)
print(inv_A)
print(torch.mm(A, inv_A))
print(torch.mm(B, inv_A))