'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.histogram\ntorch.Tensor.histogram(_input_tensor, input, bins, *, range=None, weight=None, density=False)\n'
import torch
input = torch.rand(100)
histogram = torch.Tensor.histogram(input, bins=10)
print(histogram)