'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.atanh\ntorch.Tensor.atanh(_input_tensor)\n'
import torch
_input_tensor = torch.randn(1, 3, 4, 4)
_output_tensor = torch.Tensor.atanh(_input_tensor)
print('Input tensor: {}'.format(_input_tensor))
print('Output tensor: {}'.format(_output_tensor))