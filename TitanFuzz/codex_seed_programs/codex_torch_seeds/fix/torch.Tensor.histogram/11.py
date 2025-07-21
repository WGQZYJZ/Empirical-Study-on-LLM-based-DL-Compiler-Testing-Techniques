'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.histogram\ntorch.Tensor.histogram(_input_tensor, input, bins, *, range=None, weight=None, density=False)\n'
import torch
input_data = torch.randn(100)
histogram_result = torch.Tensor.histogram(input_data, bins=3, range=((- 1), 1))
print('histogram_result: ', histogram_result)