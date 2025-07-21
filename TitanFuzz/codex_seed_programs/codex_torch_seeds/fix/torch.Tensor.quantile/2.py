'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.quantile\ntorch.Tensor.quantile(_input_tensor, q, dim=None, keepdim=False)\n'
import torch
x = torch.randn(3, 4)
print(x.quantile(0.5))
print(x.quantile(0.5, dim=0))
print(x.quantile(0.5, dim=1, keepdim=True))