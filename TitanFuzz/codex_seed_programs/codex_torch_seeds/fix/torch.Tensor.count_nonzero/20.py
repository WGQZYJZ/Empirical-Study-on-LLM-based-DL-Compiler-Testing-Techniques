'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.count_nonzero\ntorch.Tensor.count_nonzero(_input_tensor, dim=None)\n'
import torch
import torch
_input_tensor = torch.randint(0, 2, (2, 3))
print('Input Tensor:\n', _input_tensor)
_output_tensor = _input_tensor.count_nonzero()
print('Output Tensor:\n', _output_tensor)