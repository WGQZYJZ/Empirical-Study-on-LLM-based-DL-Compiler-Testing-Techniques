'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arcsin\ntorch.arcsin(input, *, out=None)\n'
import torch
import numpy as np
a = torch.tensor([(- 1.0), (- 0.5), 0.0, 0.5, 1.0])
print(torch.arcsin(a))