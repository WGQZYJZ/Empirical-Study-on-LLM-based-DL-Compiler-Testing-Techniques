'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.t\ntorch.Tensor.t(_input_tensor)\n'
import torch
_input_tensor = torch.rand(2, 3)
print('Input Tensor: ', _input_tensor)
_transposed_tensor = _input_tensor.t()
print('Transposed Tensor: ', _transposed_tensor)