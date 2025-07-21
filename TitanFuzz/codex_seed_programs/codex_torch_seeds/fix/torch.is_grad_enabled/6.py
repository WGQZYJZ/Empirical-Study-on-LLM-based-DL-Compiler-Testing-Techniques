'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_grad_enabled\ntorch.is_grad_enabled()\n'
import torch
x = torch.randn(1, requires_grad=True)
print('x = ', x)
print('torch.is_grad_enabled() = ', torch.is_grad_enabled())
with torch.no_grad():
    print('torch.is_grad_enabled() = ', torch.is_grad_enabled())
    y = torch.randn(1)
    print('y = ', y)