'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.requires_grad_\ntorch.Tensor.requires_grad_(_input_tensor, requires_grad=True)\n'
import torch
input_tensor = torch.randn(4, 4)
torch.Tensor.requires_grad_(input_tensor, requires_grad=True)
print('input_tensor = ', input_tensor)
print('input_tensor.requires_grad = ', input_tensor.requires_grad)