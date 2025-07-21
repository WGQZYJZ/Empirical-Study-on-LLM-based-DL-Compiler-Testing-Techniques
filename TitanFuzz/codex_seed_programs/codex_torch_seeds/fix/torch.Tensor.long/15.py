'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.long\ntorch.Tensor.long(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.rand(2, 3)
print('Input tensor: {}'.format(_input_tensor))
_output_tensor = torch.Tensor.long(_input_tensor)
print('Output tensor: {}'.format(_output_tensor))
_output_tensor = torch.Tensor.long(_input_tensor, memory_format=torch.preserve_format)
print('Output tensor: {}'.format(_output_tensor))