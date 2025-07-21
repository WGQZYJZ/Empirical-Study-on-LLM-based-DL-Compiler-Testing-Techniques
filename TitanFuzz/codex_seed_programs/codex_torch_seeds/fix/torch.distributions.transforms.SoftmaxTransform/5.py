'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.SoftmaxTransform\ntorch.distributions.transforms.SoftmaxTransform(cache_size=0)\n'
import torch
from torch.distributions import transforms
import numpy as np
data = np.random.randn(5, 10)
data = torch.from_numpy(data)
softmax_transform = transforms.SoftmaxTransform(cache_size=0)
print(softmax_transform(data))