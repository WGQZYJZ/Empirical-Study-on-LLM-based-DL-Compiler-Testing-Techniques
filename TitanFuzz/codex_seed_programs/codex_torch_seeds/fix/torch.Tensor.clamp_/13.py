'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clamp_\ntorch.Tensor.clamp_(_input_tensor, min=None, max=None)\n'
import torch
input_tensor = torch.randn(2, 3)
print('Input Tensor: ', input_tensor)
torch.Tensor.clamp_(input_tensor, min=(- 0.5), max=0.5)
print('Output Tensor: ', input_tensor)