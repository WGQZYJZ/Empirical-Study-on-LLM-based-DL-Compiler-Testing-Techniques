'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.quantile\ntorch.Tensor.quantile(_input_tensor, q, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(100, 3)
print('Input tensor: ', input_tensor)
print('Quantile along the first dimension: ', input_tensor.quantile(0.5, dim=0))
print('Quantile along the second dimension: ', input_tensor.quantile(0.5, dim=1))
print('Quantile along the first dimension with keepdim: ', input_tensor.quantile(0.5, dim=0, keepdim=True))
print('Quantile along the second dimension with keepdim: ', input_tensor.quantile(0.5, dim=1, keepdim=True))