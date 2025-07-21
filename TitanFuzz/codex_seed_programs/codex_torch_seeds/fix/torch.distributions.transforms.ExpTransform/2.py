'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.ExpTransform\ntorch.distributions.transforms.ExpTransform(cache_size=0)\n'
import torch
import torch.distributions as dist
import numpy as np
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float)
print(input_data)
transformed_data = dist.transforms.ExpTransform().inv(input_data)
print(transformed_data)