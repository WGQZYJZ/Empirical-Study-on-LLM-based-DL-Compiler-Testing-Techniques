'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clamp\ntorch.Tensor.clamp(_input_tensor, min=None, max=None)\n'
import torch
input_tensor = torch.randn(1, 3)
print('Input tensor: ', input_tensor)
min_value = 0.5
max_value = 1.5
output_tensor = input_tensor.clamp(min_value, max_value)
print('Output tensor: ', output_tensor)