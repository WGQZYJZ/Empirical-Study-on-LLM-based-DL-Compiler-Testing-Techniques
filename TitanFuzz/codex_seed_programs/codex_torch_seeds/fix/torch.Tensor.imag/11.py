'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.imag\ntorch.Tensor.imag(_input_tensor, )\n'
import torch
_input_tensor = torch.rand(3, 3)
_output_tensor = torch.Tensor.imag(_input_tensor)
print('Input tensor: ', _input_tensor)
print('Output tensor: ', _output_tensor)