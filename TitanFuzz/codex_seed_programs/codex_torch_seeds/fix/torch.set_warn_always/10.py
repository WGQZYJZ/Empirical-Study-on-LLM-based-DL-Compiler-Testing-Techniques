'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_warn_always\ntorch.set_warn_always(b)\n'
import torch
x = torch.randn(1, 3, 3, 3)
torch.set_warn_always(False)
print(x)