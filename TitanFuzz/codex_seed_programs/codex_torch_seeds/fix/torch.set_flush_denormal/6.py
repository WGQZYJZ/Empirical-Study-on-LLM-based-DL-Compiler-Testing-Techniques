'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_flush_denormal\ntorch.set_flush_denormal(mode)\n'
import torch
import numpy as np
x = torch.randn(1, 1, 3, 3, dtype=torch.float32)
y = torch.randn(1, 1, 3, 3, dtype=torch.float32)
torch.set_flush_denormal(True)
z = (x + y)
print('{}'.format(z))