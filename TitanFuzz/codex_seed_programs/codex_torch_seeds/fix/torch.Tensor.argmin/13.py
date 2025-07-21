'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.argmin\ntorch.Tensor.argmin(_input_tensor, dim=None, keepdim=False)\n'
import torch
_input_tensor = torch.randn(3, 3)
print(_input_tensor)
_dim = 0
_keepdim = False
_output_tensor = torch.Tensor.argmin(_input_tensor, dim=_dim, keepdim=_keepdim)
print(_output_tensor)