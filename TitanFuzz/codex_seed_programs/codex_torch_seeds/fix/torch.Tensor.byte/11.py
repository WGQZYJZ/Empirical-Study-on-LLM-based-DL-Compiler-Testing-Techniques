'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.byte\ntorch.Tensor.byte(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.randn(2, 3, 5, 7)
_output_tensor = _input_tensor.byte()
print('Input tensor:\n', _input_tensor)
print('Output tensor:\n', _output_tensor)