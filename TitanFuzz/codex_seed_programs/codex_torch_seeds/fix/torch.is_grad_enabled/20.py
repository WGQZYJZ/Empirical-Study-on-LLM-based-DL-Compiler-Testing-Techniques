'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_grad_enabled\ntorch.is_grad_enabled()\n'
import torch
x = torch.randn(1, requires_grad=True)
print(torch.is_grad_enabled())
with torch.set_grad_enabled(False):
    print(torch.is_grad_enabled())