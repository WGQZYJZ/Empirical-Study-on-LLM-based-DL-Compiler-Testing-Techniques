'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.empty\ntorch.empty(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False, pin_memory=False, memory_format=torch.contiguous_format)\n'
import torch
print(torch.empty(2, 3))
print(torch.empty(2, 3, dtype=torch.int))
print(torch.empty(2, 3, dtype=torch.double))
print(torch.empty(2, 3, dtype=torch.float))
print(torch.empty(2, 3, dtype=torch.int, device='cpu'))
print(torch.empty(2, 3, dtype=torch.int, device='cuda:0'))