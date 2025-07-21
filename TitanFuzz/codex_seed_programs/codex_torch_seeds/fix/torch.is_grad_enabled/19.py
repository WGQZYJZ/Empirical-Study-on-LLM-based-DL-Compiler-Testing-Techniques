'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_grad_enabled\ntorch.is_grad_enabled()\n'
import torch
x = torch.tensor([1.0, 2.0, 3.0, 4.0], requires_grad=True)
y = torch.tensor([2.0, 2.0, 2.0, 2.0])
print(torch.is_grad_enabled())
torch.set_grad_enabled(False)
print(torch.is_grad_enabled())
torch.set_grad_enabled(True)
print(torch.is_grad_enabled())
with torch.no_grad():
    print(torch.is_grad_enabled())
print(torch.is_grad_enabled())