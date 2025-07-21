'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.randperm\ntorch.randperm(n, *, generator=None, out=None, dtype=torch.int64, layout=torch.strided, device=None, requires_grad=False, pin_memory=False)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
print('Task 3: Call the API torch.randperm')
print(torch.randperm(5))
print(torch.randperm(5, dtype=torch.float))
print(torch.randperm(5, dtype=torch.double))
print(torch.randperm(5, dtype=torch.int))
print(torch.randperm(5, dtype=torch.long))
print(torch.randperm(5, dtype=torch.short))
print(torch.randperm(5, dtype=torch.half))
print(torch.randperm(5, dtype=torch.uint8))
print(torch.randperm(5, dtype=torch.int8))