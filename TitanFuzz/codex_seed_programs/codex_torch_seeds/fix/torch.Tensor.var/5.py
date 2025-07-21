'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.var\ntorch.Tensor.var(_input_tensor, dim, unbiased=True, keepdim=False)\n'
import torch
input_data = torch.randn(1, 3)
print('Input data: ', input_data)
print('Variance: ', input_data.var(dim=0))