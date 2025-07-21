'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clamp_\ntorch.Tensor.clamp_(_input_tensor, min=None, max=None)\n'
import torch
input_tensor = torch.tensor([(- 1), (- 0.5), 0, 0.5, 1])
clamped_tensor = input_tensor.clamp_(min=(- 0.5), max=0.5)
print('input_tensor: ', input_tensor)
print('clamped_tensor: ', clamped_tensor)
'\nTask 4: Call the API torch.clamp\ntorch.clamp(_input_tensor, min=None, max=None)\n'
clamped_tensor = torch.clamp(input_tensor, min=(- 0.5), max=0.5)
print('input_tensor: ', input_tensor)
print('clamped_tensor: ', clamped_tensor)