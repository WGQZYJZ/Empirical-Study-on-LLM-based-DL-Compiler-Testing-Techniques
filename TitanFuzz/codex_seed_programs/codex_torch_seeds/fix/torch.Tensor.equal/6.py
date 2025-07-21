'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.equal\ntorch.Tensor.equal(_input_tensor, other)\n'
import torch
_input_tensor = torch.randn(2, 3)
other = torch.randn(2, 3)
_output_tensor = _input_tensor.equal(other)
print('input_tensor:')
print(_input_tensor)
print('output_tensor:')
print(_output_tensor)