'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nanquantile\ntorch.Tensor.nanquantile(_input_tensor, q, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.Tensor([[1, 3, 5, 7], [2, 4, 6, 8], [10, 9, 8, 7]])
quantile_tensor = input_tensor.nanquantile(0.5)
print('input_tensor:')
print(input_tensor)
print('quantile_tensor:')
print(quantile_tensor)