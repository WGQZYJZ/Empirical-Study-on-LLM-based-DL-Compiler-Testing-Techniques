'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.argmin\ntorch.Tensor.argmin(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(5, 3)
print('input_tensor.argmin(dim=0) = ', input_tensor.argmin(dim=0))
print('input_tensor.argmin(dim=1) = ', input_tensor.argmin(dim=1))
print('input_tensor.argmin(dim=0, keepdim=True) = ', input_tensor.argmin(dim=0, keepdim=True))
print('input_tensor.argmin(dim=1, keepdim=True) = ', input_tensor.argmin(dim=1, keepdim=True))