'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.randint_like\ntorch.randint_like(input, low=0, high, *, dtype=None, layout=torch.strided, device=None, requires_grad=False, memory_format=torch.preserve_format)\n'
import torch
x = torch.empty(5, 3)
print(torch.randint_like(x, low=0, high=10))
x = torch.empty(5, 3).long()
print(torch.randint_like(x, low=0, high=10))