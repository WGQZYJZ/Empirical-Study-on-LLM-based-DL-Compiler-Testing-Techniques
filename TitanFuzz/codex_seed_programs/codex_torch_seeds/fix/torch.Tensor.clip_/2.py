'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clip_\ntorch.Tensor.clip_(_input_tensor, min=None, max=None)\n'
import torch
input_tensor = torch.randn(10, requires_grad=True)
print('Input tensor: ', input_tensor)
print('Clip_: ', input_tensor.clip_(min=(- 0.5), max=0.5))
print('Clip_: ', input_tensor.clip_(min=0.5))
print('Clip_: ', input_tensor.clip_(max=0.5))