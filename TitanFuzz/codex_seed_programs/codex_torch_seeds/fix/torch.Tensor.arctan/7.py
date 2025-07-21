'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arctan\ntorch.Tensor.arctan(_input_tensor)\n'
import torch
_input_tensor = torch.rand(1, 3, 3)
_output_tensor = torch.Tensor.arctan(_input_tensor)
print('Input data:')
print(_input_tensor)
print('Output data:')
print(_output_tensor)