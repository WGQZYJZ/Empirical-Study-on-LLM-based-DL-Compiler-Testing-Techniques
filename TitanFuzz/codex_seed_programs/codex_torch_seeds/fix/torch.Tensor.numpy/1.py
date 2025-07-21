'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.numpy\ntorch.Tensor.numpy(_input_tensor)\n'
import torch
_input_tensor = torch.randn(2, 3)
print('Input tensor: {}'.format(_input_tensor))
_output_tensor = _input_tensor.numpy()
print('Output tensor: {}'.format(_output_tensor))
print('The type of the output tensor is: {}'.format(type(_output_tensor)))