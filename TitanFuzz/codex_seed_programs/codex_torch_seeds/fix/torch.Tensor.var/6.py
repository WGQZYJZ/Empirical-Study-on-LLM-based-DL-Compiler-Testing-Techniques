'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.var\ntorch.Tensor.var(_input_tensor, dim, unbiased=True, keepdim=False)\n'
import torch
input_tensor = torch.randn(2, 3)
print('Input tensor: ', input_tensor)
print('Variance: ', input_tensor.var(dim=None, unbiased=True, keepdim=False))