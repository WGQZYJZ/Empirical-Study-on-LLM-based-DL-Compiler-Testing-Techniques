'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.median\ntorch.Tensor.median(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.rand(5, 5)
print('Input tensor: ', input_tensor)
median = input_tensor.median()
print('Median: ', median)
median = input_tensor.median(dim=0)
print('Median: ', median)
median = input_tensor.median(dim=0, keepdim=True)
print('Median: ', median)