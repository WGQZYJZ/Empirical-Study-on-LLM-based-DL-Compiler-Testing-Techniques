'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clamp\ntorch.Tensor.clamp(_input_tensor, min=None, max=None)\n'
import torch
_input_tensor = torch.randn(5, 3)
_output_tensor = _input_tensor.clamp(min=0)
print('Input tensor:\n', _input_tensor)
print('Output tensor:\n', _output_tensor)