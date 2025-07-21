'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tile\ntorch.Tensor.tile(_input_tensor, dims)\n'
import torch
_input_tensor = torch.randn(2, 3)
_dims = (2, 1)
_output_tensor = torch.Tensor.tile(_input_tensor, _dims)
print('Input Tensor: ', _input_tensor)
print('Output Tensor: ', _output_tensor)