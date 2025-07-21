'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.floor\ntorch.Tensor.floor(_input_tensor)\n'
import torch
_input_tensor = torch.rand(5, 5)
_output_tensor = torch.Tensor.floor(_input_tensor)
print('Input Tensor', _input_tensor)
print('Output Tensor', _output_tensor)