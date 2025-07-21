'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nonzero\ntorch.Tensor.nonzero(_input_tensor, as_tuple=False)\n'
import torch
_input_tensor = torch.randn(4, 4)
print('Input tensor: ', _input_tensor)
_output_tensor = _input_tensor.nonzero()
print('Output tensor: ', _output_tensor)