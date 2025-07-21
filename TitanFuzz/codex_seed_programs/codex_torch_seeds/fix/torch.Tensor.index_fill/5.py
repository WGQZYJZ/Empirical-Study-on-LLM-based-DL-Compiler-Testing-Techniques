'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_fill\ntorch.Tensor.index_fill(_input_tensor, dim, index, value)\n'
import torch
_input_tensor = torch.randn(3, 3)
print('Input Tensor:')
print(_input_tensor)
print('\n')
_dim = 0
_index = torch.tensor([0, 2])
_value = 0.0
_output_tensor = _input_tensor.index_fill(_dim, _index, _value)
print('Output Tensor:')
print(_output_tensor)