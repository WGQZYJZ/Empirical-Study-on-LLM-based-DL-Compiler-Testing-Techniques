'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.randint\ntorch.randint(low=0, high, size, *, generator=None, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
low = 0
high = 100
size = [2, 3]
data = torch.randint(low, high, size)
print(data)
data = torch.randint(low, high, size, dtype=torch.float32)
print(data)