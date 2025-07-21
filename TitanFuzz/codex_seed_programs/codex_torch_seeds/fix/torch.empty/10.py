'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.empty\ntorch.empty(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False, pin_memory=False, memory_format=torch.contiguous_format)\n'
import torch
x = torch.randn(4, 4)
print(x)
y = torch.empty(4, 4)
print(y)