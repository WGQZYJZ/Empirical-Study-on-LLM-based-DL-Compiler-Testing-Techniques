'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_fill\ntorch.Tensor.index_fill(_input_tensor, dim, index, value)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
_input_tensor = torch.rand(2, 3)
print('Input tensor:')
print(_input_tensor)
print('Task 3: Call the API torch.Tensor.index_fill')
_dim = 1
_index = torch.LongTensor([0, 2])
_value = 1
_output_tensor = _input_tensor.index_fill(_dim, _index, _value)
print('Output tensor:')
print(_output_tensor)