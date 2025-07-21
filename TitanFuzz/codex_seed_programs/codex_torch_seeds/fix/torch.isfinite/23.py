'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isfinite\ntorch.isfinite(input)\n'
import torch
import numpy as np
input = np.random.rand(3, 3)
input = torch.from_numpy(input)
print(torch.isfinite(input))