'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_warn_always\ntorch.set_warn_always(b)\n'
import torch
x = torch.rand(10, requires_grad=True)
print(x)
torch.set_warn_always(True)
print(x)