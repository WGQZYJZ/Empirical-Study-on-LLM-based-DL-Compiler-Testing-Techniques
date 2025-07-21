'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.histogram\ntorch.Tensor.histogram(_input_tensor, input, bins, *, range=None, weight=None, density=False)\n'
import torch
import torch
input_tensor = torch.randn(100)
histogram = torch.Tensor.histogram(input_tensor, bins=10)
print(histogram)