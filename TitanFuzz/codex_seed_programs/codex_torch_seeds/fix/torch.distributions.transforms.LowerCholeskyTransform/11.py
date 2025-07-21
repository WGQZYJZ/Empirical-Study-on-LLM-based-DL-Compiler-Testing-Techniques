'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.LowerCholeskyTransform\ntorch.distributions.transforms.LowerCholeskyTransform(cache_size=0)\n'
import torch
X = torch.randn(100, 3)
lower_cholesky = torch.distributions.transforms.LowerCholeskyTransform(cache_size=0)
print(lower_cholesky)