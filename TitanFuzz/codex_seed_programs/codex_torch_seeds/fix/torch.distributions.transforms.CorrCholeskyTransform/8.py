'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.CorrCholeskyTransform\ntorch.distributions.transforms.CorrCholeskyTransform(cache_size=0)\n'
import torch
import numpy as np
x = torch.randn(3, 3)
corr_cholesky_transform = torch.distributions.transforms.CorrCholeskyTransform(cache_size=0)
corr_cholesky_transform.inv(x)