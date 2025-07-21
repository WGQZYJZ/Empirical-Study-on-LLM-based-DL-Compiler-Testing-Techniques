'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.quantile\ntorch.Tensor.quantile(_input_tensor, q, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(3, 3)
print('input_tensor:', input_tensor)
print('input_tensor.quantile(0.5):', input_tensor.quantile(0.5))
print('input_tensor.quantile(0.5, dim=0):', input_tensor.quantile(0.5, dim=0))
print('input_tensor.quantile(0.5, dim=1):', input_tensor.quantile(0.5, dim=1))
print('input_tensor.quantile(0.5, dim=1, keepdim=True):', input_tensor.quantile(0.5, dim=1, keepdim=True))