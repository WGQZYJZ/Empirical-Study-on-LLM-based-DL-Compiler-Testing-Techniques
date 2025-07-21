'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.view_as\ntorch.Tensor.view_as(_input_tensor, other)\n'
import torch
_input_tensor = torch.randn(4, 4)
_output_tensor = _input_tensor.view_as(_input_tensor)
print('input tensor: ', _input_tensor)
print('output tensor: ', _output_tensor)