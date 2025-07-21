'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.median\ntorch.Tensor.median(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(5, 4)
print('Input tensor:', input_tensor)
print('Median:', input_tensor.median())
input_tensor = torch.randn(5, 4)
print('Input tensor:', input_tensor)
print('Median:', input_tensor.median(dim=1))
input_tensor = torch.randn(5, 4)
print('Input tensor:', input_tensor)
print('Median:', input_tensor.median(dim=1, keepdim=True))