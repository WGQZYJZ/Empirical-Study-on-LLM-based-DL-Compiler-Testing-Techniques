'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isnan\ntorch.isnan(input)\n'
import torch
import numpy as np
input = np.random.randn(4, 4)
input = torch.from_numpy(input)
torch.isnan(input)