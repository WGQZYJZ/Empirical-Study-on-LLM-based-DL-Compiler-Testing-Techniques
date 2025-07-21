'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.randn\ntorch.randn(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
x = torch.randn(2, 3)
print(x)
'\nTask 4: Call the API torch.randn_like\ntorch.randn_like(input, dtype=None, layout=None, device=None, requires_grad=False)\n'
x = torch.randn_like(x, dtype=torch.float)
print(x)
'\nTask 5: Call the API torch.rand\ntorch.rand(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
x = torch.rand(2, 3)
print(x)
'\nTask 6: Call the API torch.rand_like\ntorch.rand_like(input, dtype=None, layout=None, device=None, requires_grad=False)\n'
x = torch.rand_like(x, dtype=torch.float)
print(x)