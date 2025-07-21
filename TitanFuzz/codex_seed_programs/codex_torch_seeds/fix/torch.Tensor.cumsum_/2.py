'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cumsum_\ntorch.Tensor.cumsum_(_input_tensor, dim, dtype=None)\n'
import torch
import torch
input_tensor = torch.randn(3, 4)
print('Input tensor: ', input_tensor)
output_tensor = torch.Tensor.cumsum_(input_tensor, dim=1, dtype=None)
print('Output tensor: ', output_tensor)