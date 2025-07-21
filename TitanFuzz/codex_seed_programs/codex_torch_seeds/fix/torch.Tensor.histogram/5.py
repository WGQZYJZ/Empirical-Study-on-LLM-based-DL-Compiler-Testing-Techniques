'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.histogram\ntorch.Tensor.histogram(_input_tensor, input, bins, *, range=None, weight=None, density=False)\n'
import torch
input_tensor = torch.randn(1, 10)
input = input_tensor.numpy()
bins = 10
range = ((- 10), 10)
weight = None
density = False
output = torch.Tensor.histogram(input_tensor, input, bins, range=range, weight=weight, density=density)
print(output)