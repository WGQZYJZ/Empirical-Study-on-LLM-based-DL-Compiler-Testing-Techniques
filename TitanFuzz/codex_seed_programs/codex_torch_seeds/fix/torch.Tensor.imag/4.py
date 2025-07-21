'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.imag\ntorch.Tensor.imag(_input_tensor, )\n'
import torch
_input_tensor = torch.rand(2, 3)
_output_tensor = _input_tensor.imag()
print('The input Tensor: {}'.format(_input_tensor))
print('The output Tensor: {}'.format(_output_tensor))