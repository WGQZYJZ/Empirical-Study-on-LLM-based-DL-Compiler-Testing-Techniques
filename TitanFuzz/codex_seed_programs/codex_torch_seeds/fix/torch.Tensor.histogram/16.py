'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.histogram\ntorch.Tensor.histogram(_input_tensor, input, bins, *, range=None, weight=None, density=False)\n'
import torch
import numpy as np
input = torch.randn(100)
bins = 10
hist = torch.Tensor.histogram(input, bins)
print(hist)