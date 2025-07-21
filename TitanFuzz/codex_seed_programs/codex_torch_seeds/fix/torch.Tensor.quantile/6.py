'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.quantile\ntorch.Tensor.quantile(_input_tensor, q, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(1, 2, 3)
print('input_tensor:', input_tensor)
output_tensor = torch.Tensor.quantile(input_tensor, q=0.5, dim=None, keepdim=False)
print('output_tensor:', output_tensor)