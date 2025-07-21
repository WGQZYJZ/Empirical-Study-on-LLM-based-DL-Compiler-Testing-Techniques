'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cos\ntorch.cos(input, *, out=None)\n'
import torch
import numpy as np
x = torch.tensor([0.0, (np.pi / 4), (np.pi / 2), ((np.pi * 3) / 4), np.pi, ((np.pi * 5) / 4), ((np.pi * 3) / 2), ((np.pi * 7) / 4)], dtype=torch.float)
print(torch.cos(x))
x.cos_()
print(x)