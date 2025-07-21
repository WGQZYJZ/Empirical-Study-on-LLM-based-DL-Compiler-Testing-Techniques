'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cummin\ntorch.Tensor.cummin(_input_tensor, dim)\n'
import torch
_input_tensor = torch.rand((4, 3))
print('Input data:\n', _input_tensor)
_output_tensor = torch.Tensor.cummin(_input_tensor, dim=1)
print('Output data:\n', _output_tensor)