'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.map_\ntorch.Tensor.map_(_input_tensor, tensor, callable\n'
import torch
_input_tensor = torch.rand(2, 3)
tensor = torch.rand(2, 3)
output_tensor = torch.Tensor.map_(tensor, _input_tensor, (lambda x, y: (x + y)))
print('Input Tensor: \n', _input_tensor)
print('Tensor: \n', tensor)
print('Output Tensor: \n', output_tensor)