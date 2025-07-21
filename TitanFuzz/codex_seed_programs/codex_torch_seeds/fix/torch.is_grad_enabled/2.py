'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_grad_enabled\ntorch.is_grad_enabled()\n'
import torch
x = torch.ones(2, 2, requires_grad=True)
print(x)
print(torch.is_grad_enabled())
'\nTask 4: Disable gradient calculation\ntorch.set_grad_enabled(False)\n'
torch.set_grad_enabled(False)
print(torch.is_grad_enabled())
'\nTask 5: Enable gradient calculation\ntorch.set_grad_enabled(True)\n'
torch.set_grad_enabled(True)
print(torch.is_grad_enabled())