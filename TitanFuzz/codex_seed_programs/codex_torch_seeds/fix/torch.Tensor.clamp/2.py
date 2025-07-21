'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clamp\ntorch.Tensor.clamp(_input_tensor, min=None, max=None)\n'
import torch
input_tensor = torch.rand(2, 3)
print('input_tensor: {}'.format(input_tensor))
clamped_tensor = input_tensor.clamp(min=0.3, max=0.7)
print('clamped_tensor: {}'.format(clamped_tensor))