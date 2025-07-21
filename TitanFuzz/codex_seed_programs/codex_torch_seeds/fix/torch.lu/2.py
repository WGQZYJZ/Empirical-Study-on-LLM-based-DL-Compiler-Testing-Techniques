'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lu\ntorch.lu(A, pivot=True, get_infos=False, *, out=None)\n'
import torch
A = torch.rand(3, 3)
print(A)
lu_result = torch.lu(A, pivot=True, get_infos=True)
print(lu_result)