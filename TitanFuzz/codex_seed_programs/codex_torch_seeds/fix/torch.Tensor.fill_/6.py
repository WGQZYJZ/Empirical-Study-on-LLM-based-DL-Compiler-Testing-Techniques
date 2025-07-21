'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fill_\ntorch.Tensor.fill_(_input_tensor, value)\n'
import torch
_input_tensor = torch.randn(2, 3, 4)
print('Input tensor: {}'.format(_input_tensor))
torch.Tensor.fill_(_input_tensor, value=0.5)
print('Output tensor: {}'.format(_input_tensor))