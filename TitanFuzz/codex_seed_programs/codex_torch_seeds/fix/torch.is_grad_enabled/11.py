'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_grad_enabled\ntorch.is_grad_enabled()\n'
import torch
input_data = torch.randn(3, requires_grad=True)
print(input_data)
print(torch.is_grad_enabled())
with torch.no_grad():
    print(torch.is_grad_enabled())
torch.set_grad_enabled(False)
print(torch.is_grad_enabled())
torch.set_grad_enabled(True)
print(torch.is_grad_enabled())