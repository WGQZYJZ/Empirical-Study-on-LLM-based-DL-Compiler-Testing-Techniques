'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clip_\ntorch.Tensor.clip_(_input_tensor, min=None, max=None)\n'
import torch
input_tensor = torch.randn(1, 3, 2)
print('Input data: \n', input_tensor)
output_tensor = torch.Tensor.clip_(input_tensor, min=(- 0.5), max=0.5)
print('Output data: \n', output_tensor)