'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.outer\ntorch.outer(input, vec2, *, out=None)\n'
import torch
import numpy as np
a = torch.arange(1, 4)
b = torch.arange(1, 3)
print(torch.outer(a, b))