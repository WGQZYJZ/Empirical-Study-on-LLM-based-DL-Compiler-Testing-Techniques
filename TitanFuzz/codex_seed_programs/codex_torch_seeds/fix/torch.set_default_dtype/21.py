'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_default_dtype\ntorch.set_default_dtype(d)\n'
import torch
a = torch.rand(3, 3, dtype=torch.float64)
print(a)
torch.set_default_dtype(torch.float64)
b = torch.rand(3, 3)
print(b)
print(a.dtype, b.dtype)