'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clamp\ntorch.Tensor.clamp(_input_tensor, min=None, max=None)\n'
import torch
input_tensor = torch.randn(2, 3)
print('Input tensor:', input_tensor)
output_tensor = input_tensor.clamp(min=0)
print('Output tensor:', output_tensor)