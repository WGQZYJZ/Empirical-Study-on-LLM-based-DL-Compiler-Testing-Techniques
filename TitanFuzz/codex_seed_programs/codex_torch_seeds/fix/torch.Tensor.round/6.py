'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.round\ntorch.Tensor.round(_input_tensor)\n'
import torch
_input_tensor = torch.randn(4, 4)
print('Input Tensor: \n', _input_tensor)
_output_tensor = torch.Tensor.round(_input_tensor)
print('Output Tensor: \n', _output_tensor)