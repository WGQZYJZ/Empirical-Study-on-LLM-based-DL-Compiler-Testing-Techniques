'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.requires_grad_\ntorch.Tensor.requires_grad_(_input_tensor, requires_grad=True)\n'
import torch
input_tensor = torch.randn(4, 4, dtype=torch.float)
print(input_tensor)
print(input_tensor.requires_grad)
print(input_tensor.requires_grad_())
print(input_tensor.requires_grad)
print(input_tensor.requires_grad_(False))
print(input_tensor.requires_grad)