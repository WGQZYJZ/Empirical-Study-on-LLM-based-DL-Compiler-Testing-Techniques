'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.chunk\ntorch.Tensor.chunk(_input_tensor, chunks, dim=0)\n'
import torch
_input_tensor = torch.randn(3, 4)
print('Input tensor: ', _input_tensor)
_output_tensor = _input_tensor.chunk(2, dim=0)
print('Output tensor: ', _output_tensor)