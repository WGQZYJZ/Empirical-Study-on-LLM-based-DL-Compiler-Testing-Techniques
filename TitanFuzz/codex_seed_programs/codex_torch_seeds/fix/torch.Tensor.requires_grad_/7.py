'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.requires_grad_\ntorch.Tensor.requires_grad_(_input_tensor, requires_grad=True)\n'
import torch
_input_tensor = torch.randn(10)
_input_tensor.requires_grad_(True)
print(_input_tensor)