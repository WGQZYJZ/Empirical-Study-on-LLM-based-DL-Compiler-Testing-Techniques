'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.select\ntorch.Tensor.select(_input_tensor, dim, index)\n'
import torch
input_tensor = torch.randn(4, 3)
print('input_tensor:', input_tensor)
output_tensor = torch.Tensor.select(input_tensor, 1, 2)
print('output_tensor:', output_tensor)