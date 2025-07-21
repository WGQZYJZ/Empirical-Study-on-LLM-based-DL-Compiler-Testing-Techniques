'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_grad_enabled\ntorch.is_grad_enabled()\n'
import torch
x = torch.randn(2, 2, requires_grad=True)
print(x)
print(torch.is_grad_enabled())