'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.floor_\ntorch.Tensor.floor_(_input_tensor)\n'
import torch
_input_tensor = torch.randn(2, 3)
print('input tensor: {}'.format(_input_tensor))
torch.Tensor.floor_(_input_tensor)
print('output tensor: {}'.format(_input_tensor))