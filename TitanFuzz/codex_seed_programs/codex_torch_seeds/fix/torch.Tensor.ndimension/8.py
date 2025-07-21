'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ndimension\ntorch.Tensor.ndimension(_input_tensor)\n'
import torch
_input_tensor = torch.rand(2, 3)
print('_input_tensor = ', _input_tensor)
_output = torch.Tensor.ndimension(_input_tensor)
print('_output = ', _output)