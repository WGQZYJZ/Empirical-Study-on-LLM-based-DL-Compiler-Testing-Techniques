'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.floor_\ntorch.Tensor.floor_(_input_tensor)\n'
import torch
_input_tensor = torch.randn(3, 3)
print('Input tensor: ')
print(_input_tensor)
print('Output tensor: ')
print(_input_tensor.floor_())