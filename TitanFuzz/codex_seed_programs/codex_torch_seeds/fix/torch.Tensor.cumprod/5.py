'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cumprod\ntorch.Tensor.cumprod(_input_tensor, dim, dtype=None)\n'
import torch
_input_tensor = torch.randn(3, 4)
print('Input tensor: ', _input_tensor)
print('Cumulative product: ', _input_tensor.cumprod(dim=0))