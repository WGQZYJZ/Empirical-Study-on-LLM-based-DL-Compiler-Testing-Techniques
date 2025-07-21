'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_warn_always\ntorch.set_warn_always(b)\n'
import numpy as np
import torch
x = torch.rand(3, 3)
print(x)
torch.set_warn_always(True)
torch.set_warn_always(False)