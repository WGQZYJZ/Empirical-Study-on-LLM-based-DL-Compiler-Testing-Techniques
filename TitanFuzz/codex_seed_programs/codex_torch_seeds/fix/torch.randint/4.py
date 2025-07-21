'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.randint\ntorch.randint(low=0, high, size, *, generator=None, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
x = torch.randint(low=0, high=10, size=(4, 4))
print(x)
x = torch.randint(3, 5, (4, 4))
print(x)
x = torch.randint(3, 5, (4, 4), dtype=torch.int64)
print(x)
x = torch.randint(3, 5, (4, 4), dtype=torch.int32)
print(x)
x = torch.randint(3, 5, (4, 4), dtype=torch.int16)
print(x)