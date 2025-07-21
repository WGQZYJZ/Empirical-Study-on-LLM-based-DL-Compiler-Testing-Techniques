'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.retain_grad\ntorch.Tensor.retain_grad(_input_tensor)\n'
import torch
_input_tensor = torch.randn(1, 2, 3, requires_grad=True)
print(_input_tensor)
_input_tensor.retain_grad()
print(_input_tensor.grad_fn)