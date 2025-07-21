'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nanquantile\ntorch.Tensor.nanquantile(_input_tensor, q, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
print('input_tensor: ', input_tensor)
quantile = torch.Tensor.nanquantile(input_tensor, 0.5, dim=2)
print('quantile: ', quantile)