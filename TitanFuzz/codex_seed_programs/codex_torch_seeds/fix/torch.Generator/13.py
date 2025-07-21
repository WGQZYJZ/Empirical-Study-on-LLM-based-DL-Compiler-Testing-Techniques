"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Generator\ntorch.Generator(device='cpu')\n"
import torch
import numpy as np
np.random.seed(0)
x = np.random.rand(2, 3)
torch.Generator(device='cpu')