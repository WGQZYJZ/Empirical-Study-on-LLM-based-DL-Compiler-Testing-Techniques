'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.quantile\ntorch.Tensor.quantile(_input_tensor, q, dim=None, keepdim=False)\n'
import torch
import torch
input_tensor = torch.rand(2, 3, 4)
print(torch.Tensor.quantile(input_tensor, 0.5, dim=1))
print(torch.Tensor.quantile(input_tensor, 0.5, dim=1, keepdim=True))