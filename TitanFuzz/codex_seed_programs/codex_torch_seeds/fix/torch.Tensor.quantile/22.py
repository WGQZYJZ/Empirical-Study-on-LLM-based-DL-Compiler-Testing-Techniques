'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.quantile\ntorch.Tensor.quantile(_input_tensor, q, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input tensor: \n', input_tensor)
q = torch.tensor([0.25, 0.5, 0.75])
print('Quantile: \n', input_tensor.quantile(q))
print('Quantile: \n', input_tensor.quantile(q, dim=1))