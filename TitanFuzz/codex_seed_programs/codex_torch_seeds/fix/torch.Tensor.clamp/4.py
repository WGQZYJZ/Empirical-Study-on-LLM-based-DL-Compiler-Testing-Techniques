'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clamp\ntorch.Tensor.clamp(_input_tensor, min=None, max=None)\n'
import torch
input_tensor = torch.randn(4, 4)
print('Input tensor: {}'.format(input_tensor))
min_value = (- 0.5)
max_value = 0.5
output_tensor = input_tensor.clamp(min_value, max_value)
print('Output tensor: {}'.format(output_tensor))