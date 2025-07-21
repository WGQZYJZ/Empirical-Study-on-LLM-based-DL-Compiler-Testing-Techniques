'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.retain_grad\ntorch.Tensor.retain_grad(_input_tensor)\n'
import torch
import torch
input_tensor = torch.randn(2, 3, requires_grad=True)
input_tensor.retain_grad()
print(input_tensor.requires_grad)
print(input_tensor.grad_fn)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.retain_grad\ntorch.Tensor.retain_grad(_input_tensor)\n'
import torch
import torch
input_tensor = torch.randn(2, 3, requires_grad=True)
input_tensor.retain_grad()
print(input_tensor.requires_grad)
print