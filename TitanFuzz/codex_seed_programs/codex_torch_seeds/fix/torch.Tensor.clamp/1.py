'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clamp\ntorch.Tensor.clamp(_input_tensor, min=None, max=None)\n'
import torch
input_tensor = torch.randn(10)
print('Input Tensor: ', input_tensor)
clamped_tensor = input_tensor.clamp(min=0.0)
print('Clamped Tensor: ', clamped_tensor)