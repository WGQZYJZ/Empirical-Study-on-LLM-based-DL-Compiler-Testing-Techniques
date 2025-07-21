'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.seed\ntorch.seed()\n'
import torch
import numpy as np
torch.seed()
np.random.seed(1)
torch.rand(3, 3)
torch.randn(3, 3)
torch.randperm(5)
torch.normal(torch.arange(1.0, 11.0), torch.arange(1, 0, (- 0.1)))
torch.bernoulli(torch.arange(0.1, 1.0, 0.1))