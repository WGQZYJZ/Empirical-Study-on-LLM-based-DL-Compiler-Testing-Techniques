'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cumprod_\ntorch.Tensor.cumprod_(_input_tensor, dim, dtype=None)\n'
import torch
input_tensor = torch.randn(2, 3)
print('Input tensor: ', input_tensor)
output_tensor = torch.Tensor.cumprod_(input_tensor, dim=1)
print('Output tensor: ', output_tensor)