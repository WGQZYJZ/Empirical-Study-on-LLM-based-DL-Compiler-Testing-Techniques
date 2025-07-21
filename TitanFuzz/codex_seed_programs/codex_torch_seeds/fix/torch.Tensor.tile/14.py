'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tile\ntorch.Tensor.tile(_input_tensor, dims)\n'
import torch
_input_tensor = torch.randn(2, 3)
print('Input tensor: ', _input_tensor)
_dims = (2, 1)
_output_tensor = _input_tensor.tile(_dims)
print('Output tensor: ', _output_tensor)