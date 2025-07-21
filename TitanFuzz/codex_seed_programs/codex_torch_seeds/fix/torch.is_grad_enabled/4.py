'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_grad_enabled\ntorch.is_grad_enabled()\n'
import torch
a = torch.randn(2, 2, requires_grad=True)
print(a)
print(torch.is_grad_enabled())
with torch.no_grad():
    print(a.requires_grad)
    print(torch.is_grad_enabled())