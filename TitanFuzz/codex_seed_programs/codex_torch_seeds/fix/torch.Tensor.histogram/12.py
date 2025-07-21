'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.histogram\ntorch.Tensor.histogram(_input_tensor, input, bins, *, range=None, weight=None, density=False)\n'
import torch
input_tensor = torch.randn(100)
histogram = input_tensor.histogram(10, 0, 1)
print(histogram)