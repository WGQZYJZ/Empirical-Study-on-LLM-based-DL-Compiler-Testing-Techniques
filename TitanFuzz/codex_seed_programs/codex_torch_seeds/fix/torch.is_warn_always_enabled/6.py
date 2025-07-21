'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_warn_always_enabled\ntorch.is_warn_always_enabled()\n'
import torch
x = torch.ones(2, 2, requires_grad=True)
print(x)
torch.is_warn_always_enabled()