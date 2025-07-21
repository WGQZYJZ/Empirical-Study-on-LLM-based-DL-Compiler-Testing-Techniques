'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cumprod_\ntorch.Tensor.cumprod_(_input_tensor, dim, dtype=None)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input_tensor = torch.randn(2, 3, 4, 5)
print('input_tensor = ', input_tensor)
print('Task 3: Call the API torch.Tensor.cumprod_')
print('torch.Tensor.cumprod_(input_tensor, dim=0) = ', torch.Tensor.cumprod_(input_tensor, dim=0))
print('torch.Tensor.cumprod_(input_tensor, dim=1) = ', torch.Tensor.cumprod_(input_tensor, dim=1))
print('torch.Tensor.cumprod_(input_tensor, dim=2) = ', torch.Tensor.cumprod_(input_tensor, dim=2))