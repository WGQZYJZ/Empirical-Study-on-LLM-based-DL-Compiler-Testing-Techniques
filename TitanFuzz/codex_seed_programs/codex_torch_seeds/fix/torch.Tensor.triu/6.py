'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.triu\ntorch.Tensor.triu(_input_tensor, diagonal=0)\n'
import torch
_input_tensor = torch.rand(2, 3)
print('Input tensor: ', _input_tensor)
_output_tensor = _input_tensor.triu(diagonal=0)
print('Output tensor: ', _output_tensor)