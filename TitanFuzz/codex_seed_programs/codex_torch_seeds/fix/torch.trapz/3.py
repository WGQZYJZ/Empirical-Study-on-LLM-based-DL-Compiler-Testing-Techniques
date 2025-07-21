'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.trapz\ntorch.trapz(y, *, dx=1, dim=-1)\n'
import torch
x = torch.randn(1, 10)
y = torch.randn(1, 10)
print(torch.trapz(y, x=x))
x = torch.randn(10, 10)
y = torch.randn(10, 10)
print(torch.trapz(y, x=x, dim=1))
x = torch.randn(10, 10)
y = torch.randn(10, 10)
print(torch.trapz(y, x=x, dim=0))