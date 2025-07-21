'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.roll\ntorch.Tensor.roll(_input_tensor, shifts, dims)\n'
import torch
_input_tensor = torch.randn(2, 3)
print('Input Tensor:')
print(_input_tensor)
_shifts = [1, 2]
_dims = [0, 1]
_output_tensor = torch.Tensor.roll(_input_tensor, _shifts, _dims)
print('Output Tensor:')
print(_output_tensor)