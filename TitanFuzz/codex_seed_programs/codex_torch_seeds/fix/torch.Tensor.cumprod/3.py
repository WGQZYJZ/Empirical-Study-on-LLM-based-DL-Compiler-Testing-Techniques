'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cumprod\ntorch.Tensor.cumprod(_input_tensor, dim, dtype=None)\n'
import torch
_input_tensor = torch.randn(4, 4)
print('Input tensor:', _input_tensor)
print('Output tensor:', _input_tensor.cumprod(dim=1))