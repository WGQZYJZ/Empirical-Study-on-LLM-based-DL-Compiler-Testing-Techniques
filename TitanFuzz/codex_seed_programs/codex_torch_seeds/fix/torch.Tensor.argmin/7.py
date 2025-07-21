'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.argmin\ntorch.Tensor.argmin(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(5, 4)
print('input_tensor:', input_tensor)
print('torch.Tensor.argmin(input_tensor, dim=0, keepdim=True):', torch.Tensor.argmin(input_tensor, dim=0, keepdim=True))
print('torch.Tensor.argmin(input_tensor, dim=1, keepdim=True):', torch.Tensor.argmin(input_tensor, dim=1, keepdim=True))