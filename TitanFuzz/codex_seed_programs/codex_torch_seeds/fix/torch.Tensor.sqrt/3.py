'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sqrt\ntorch.Tensor.sqrt(_input_tensor)\n'
import torch
_input_tensor = torch.rand(2, 3)
_output_tensor = torch.Tensor.sqrt(_input_tensor)
print('Input tensor: ', _input_tensor)
print('Output tensor: ', _output_tensor)