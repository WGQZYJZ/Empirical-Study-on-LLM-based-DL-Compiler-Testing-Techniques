'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.randint\ntorch.randint(low=0, high, size, *, generator=None, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
x = torch.randint(low=0, high=10, size=(4, 4))
print(x)
y = torch.randint(low=0, high=10, size=(4, 4), dtype=torch.float32)
print(y)
z = torch.randint(low=0, high=10, size=(4, 4), dtype=torch.float32, device='cuda')
print(z)