'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_grad_enabled\ntorch.is_grad_enabled()\n'
import torch
x = torch.tensor([1.0, 2.0, 3.0, 4.0], requires_grad=True)
y = (2 * x)
z = y.view(2, 2)
print(z)
print(torch.is_grad_enabled())