'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cumprod_\ntorch.Tensor.cumprod_(_input_tensor, dim, dtype=None)\n'
import torch
input_tensor = torch.randn(3, 3)
torch.Tensor.cumprod_(input_tensor, dim=1)
print('input_tensor: ', input_tensor)
print('input_tensor.cumprod(dim=1): ', input_tensor.cumprod(dim=1))