'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.frac_\ntorch.Tensor.frac_(_input_tensor)\n'
import torch
_input_tensor = torch.randn(1, 2, 3, 4, 5)
_output_tensor = torch.Tensor.frac_(_input_tensor)
print('Input tensor:\n', _input_tensor)
print('Output tensor:\n', _output_tensor)