'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.quantile\ntorch.Tensor.quantile(_input_tensor, q, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input tensor is: ')
print(input_tensor)
quantile_value = torch.Tensor.quantile(input_tensor, 0.5)
print('Quantile value is: ')
print(quantile_value)