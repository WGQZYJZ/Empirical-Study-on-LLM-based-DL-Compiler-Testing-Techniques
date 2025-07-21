'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.random.seed\ntorch.random.seed()\n'
import torch
import numpy as np
x = np.random.randn(1, 3, 224, 224)
x = torch.from_numpy(x)
torch.random.seed()