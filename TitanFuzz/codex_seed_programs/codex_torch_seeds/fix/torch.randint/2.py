'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.randint\ntorch.randint(low=0, high, size, *, generator=None, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
low = 2
high = 10
size = (4, 5)
tensor = torch.randint(low, high, size)
print(tensor)
print(tensor.dtype)
print(tensor.device)
print(tensor.layout)
print(tensor.shape)
print(tensor.ndim)
print(tensor.numel())
print(tensor.size())