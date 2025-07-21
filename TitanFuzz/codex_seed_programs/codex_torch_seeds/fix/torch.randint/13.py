'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.randint\ntorch.randint(low=0, high, size, *, generator=None, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
n = 10
low = 0
high = 100
x = torch.randint(low, high, (n,), dtype=torch.int64)
print(x)