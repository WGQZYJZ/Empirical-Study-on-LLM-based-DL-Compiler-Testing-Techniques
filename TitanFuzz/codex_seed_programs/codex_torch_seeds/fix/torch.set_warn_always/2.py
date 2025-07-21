'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_warn_always\ntorch.set_warn_always(b)\n'
import torch
x = torch.randn(1, requires_grad=True)
y = torch.randn(1, requires_grad=True)
torch.set_warn_always(True)
print((x + y))
torch.set_warn_always(False)
print((x + y))