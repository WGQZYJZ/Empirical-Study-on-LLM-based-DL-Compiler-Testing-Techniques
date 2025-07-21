'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_warn_always\ntorch.set_warn_always(b)\n'
import torch
import numpy as np
torch.set_warn_always(True)
x = torch.randn(10)
print(x)
torch.set_warn_always(False)
x = torch.randn(10)
print(x)