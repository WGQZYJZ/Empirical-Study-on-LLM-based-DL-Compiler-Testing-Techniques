'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.argmin\ntorch.Tensor.argmin(_input_tensor, dim=None, keepdim=False)\n'
import torch
_input_tensor = torch.randn(4, 4)
print(_input_tensor)
print(_input_tensor.argmin())
print(_input_tensor.argmin(dim=0))
print(_input_tensor.argmin(dim=1))
print(_input_tensor.argmin(dim=0, keepdim=True))
print(_input_tensor.argmin(dim=1, keepdim=True))