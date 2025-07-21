'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nanquantile\ntorch.Tensor.nanquantile(_input_tensor, q, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(3, 3)
input_tensor[(1, 1)] = float('nan')
print(input_tensor)
print(torch.Tensor.nanquantile(input_tensor, q=0.5))
print(torch.Tensor.nanquantile(input_tensor, q=0.5, dim=0))
print(torch.Tensor.nanquantile(input_tensor, q=0.5, dim=1, keepdim=True))