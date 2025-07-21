'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tile\ntorch.Tensor.tile(_input_tensor, dims)\n'
import torch
_input_tensor = torch.randn(1, 2, 3)
print('Input Tensor: ', _input_tensor)
_output_tensor = torch.Tensor.tile(_input_tensor, dims=(1, 3))
print('Output Tensor: ', _output_tensor)
_output_tensor = torch.Tensor.tile(_input_tensor, dims=(2, 1))
print('Output Tensor: ', _output_tensor)
_output_tensor = torch.Tensor.tile(_input_tensor, dims=(2, 3))
print('Output Tensor: ', _output_tensor)
_output_tensor = torch.Tensor.tile(_input_tensor, dims=(3, 2))
print('Output Tensor: ', _output_tensor)