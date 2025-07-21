'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rand\ntorch.rand(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
x = torch.rand(5, 3)
print(x)
'\nTask 4: Call the API torch.randn\ntorch.randn(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
x = torch.randn(5, 3)
print(x)
'\nTask 5: Call the API torch.randint\ntorch.randint(low, high, size, *, generator=None, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
x = torch.randint(5, 10, (5, 3))
print(x)
'\nTask 6: Call the API torch.randperm\ntorch.randperm(n, *, generator=None, out=None)\n'
x = torch.randperm(5)
print(x)