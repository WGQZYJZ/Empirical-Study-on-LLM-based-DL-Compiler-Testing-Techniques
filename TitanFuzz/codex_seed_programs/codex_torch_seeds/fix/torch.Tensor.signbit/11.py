'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.signbit\ntorch.Tensor.signbit(_input_tensor)\n'
import torch
'\nTask 2: Generate input data\n'
_input_tensor = torch.randn(2, 3)
print('Input Tensor:\n', _input_tensor)
'\nTask 3: Call the API torch.Tensor.signbit\ntorch.Tensor.signbit(_input_tensor)\n'
_output_tensor = _input_tensor.signbit()
print('Output Tensor:\n', _output_tensor)