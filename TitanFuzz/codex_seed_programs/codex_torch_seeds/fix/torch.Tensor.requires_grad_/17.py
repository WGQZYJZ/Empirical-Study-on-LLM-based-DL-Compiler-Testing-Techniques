'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.requires_grad_\ntorch.Tensor.requires_grad_(_input_tensor, requires_grad=True)\n'
import torch
import torch
input_tensor = torch.randn(5, 3)
input_tensor.requires_grad_(True)
print(input_tensor)
print(input_tensor.grad_fn)