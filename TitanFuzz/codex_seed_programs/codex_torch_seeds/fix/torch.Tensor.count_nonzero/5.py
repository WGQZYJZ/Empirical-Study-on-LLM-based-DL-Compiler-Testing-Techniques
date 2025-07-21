'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.count_nonzero\ntorch.Tensor.count_nonzero(_input_tensor, dim=None)\n'
import torch
_input_tensor = torch.rand(2, 3, 4)
print('Input data:\n', _input_tensor)
_output_tensor = torch.Tensor.count_nonzero(_input_tensor, dim=None)
print('Output data:\n', _output_tensor)