'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clamp\ntorch.Tensor.clamp(_input_tensor, min=None, max=None)\n'
import torch
input_tensor = torch.rand(4, 4)
print('input_tensor:', input_tensor)
_min = 0.5
_max = 0.8
print('min:', _min, 'max:', _max)
output_tensor = input_tensor.clamp(_min, _max)
print('output_tensor:', output_tensor)
'\nTask 4: Call the API torch.Tensor.clamp_\ntorch.Tensor.clamp_(_input_tensor, min=None, max=None)\n'
input_tensor = torch.rand(4, 4)
print('input_tensor:', input_tensor)
_min = 0.5
_max = 0.8
print('min:', _min, 'max:', _max)
output_tensor = input_tensor.clamp_(_min, _max)
print('output_tensor:', output_tensor)