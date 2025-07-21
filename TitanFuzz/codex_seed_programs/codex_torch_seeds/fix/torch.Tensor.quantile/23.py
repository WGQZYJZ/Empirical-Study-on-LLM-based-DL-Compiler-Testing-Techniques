'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.quantile\ntorch.Tensor.quantile(_input_tensor, q, dim=None, keepdim=False)\n'
import torch
import torch
input_tensor = torch.randn(4, 4)
quantile_value = torch.Tensor.quantile(input_tensor, 0.5, dim=None, keepdim=False)
print(quantile_value)