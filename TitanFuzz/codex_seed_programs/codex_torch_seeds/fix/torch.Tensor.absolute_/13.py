'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.absolute_\ntorch.Tensor.absolute_(_input_tensor)\n'
import torch
_input_tensor = torch.randn(2, 3, 4)
_output_tensor = torch.Tensor.absolute_(_input_tensor)
print(_input_tensor)
print(_output_tensor)