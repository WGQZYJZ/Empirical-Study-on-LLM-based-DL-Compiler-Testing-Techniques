'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clone\ntorch.Tensor.clone(_input_tensor, *, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.randn(2, 3)
print('Input tensor: {}'.format(_input_tensor))
_output_tensor = _input_tensor.clone()
print('Output tensor: {}'.format(_output_tensor))
print('Type of input tensor: {}'.format(type(_input_tensor)))
print('Type of output tensor: {}'.format(type(_output_tensor)))