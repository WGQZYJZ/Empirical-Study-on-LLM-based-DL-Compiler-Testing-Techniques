'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clip_\ntorch.Tensor.clip_(_input_tensor, min=None, max=None)\n'
import torch
input_tensor = torch.randn(3, 3)
print('input_tensor:', input_tensor)
output_tensor = torch.Tensor.clip_(input_tensor, min=(- 1), max=1)
print('output_tensor:', output_tensor)