'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.ExpTransform\ntorch.distributions.transforms.ExpTransform(cache_size=0)\n'
import torch
from torch.distributions.transforms import ExpTransform
data = torch.randn(2, 3)
print('Input data: ', data)
exp_transform = ExpTransform(cache_size=0)
print('Output data: ', exp_transform(data))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.LowerCholeskyTransform\ntorch.distributions.transforms.LowerCholeskyTransform(validate_args=False)\n'
import torch
from torch.distributions.transforms import LowerCholeskyTransform
data = torch.randn(2, 3)
print('Input data: ', data)