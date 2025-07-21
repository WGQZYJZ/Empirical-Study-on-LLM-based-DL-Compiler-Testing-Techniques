'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_grad_enabled\ntorch.set_grad_enabled(mode)\n'
import torch
x = torch.ones(2, 2, requires_grad=True)
print(x)
torch.set_grad_enabled(True)
print(x.requires_grad)
torch.set_grad_enabled(False)
print(x.requires_grad)