'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.half\ntorch.Tensor.half(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.randn(4, 4)
_output_tensor = _input_tensor.half()
print('Input tensor:', _input_tensor)
print('Output tensor:', _output_tensor)