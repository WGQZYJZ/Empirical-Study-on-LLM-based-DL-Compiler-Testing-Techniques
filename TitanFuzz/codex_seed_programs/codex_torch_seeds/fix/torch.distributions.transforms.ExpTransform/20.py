'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.ExpTransform\ntorch.distributions.transforms.ExpTransform(cache_size=0)\n'
import torch
import numpy as np
from torch.distributions.transforms import ExpTransform
x = np.random.randn(100)
x = torch.tensor(x)
print('Input data:', x)
exp_transform = ExpTransform()
y = exp_transform(x)
print('Output data:', y)