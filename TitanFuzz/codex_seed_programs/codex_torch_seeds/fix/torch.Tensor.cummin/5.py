'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cummin\ntorch.Tensor.cummin(_input_tensor, dim)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
print('input_tensor:', input_tensor)
output_tensor = input_tensor.cummin(1)
print('output_tensor:', output_tensor)