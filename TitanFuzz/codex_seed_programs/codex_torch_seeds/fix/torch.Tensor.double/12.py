'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.double\ntorch.Tensor.double(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.randn(2, 3, 4)
print('_input_tensor:', _input_tensor)
_output_tensor = _input_tensor.double()
print('_output_tensor:', _output_tensor)