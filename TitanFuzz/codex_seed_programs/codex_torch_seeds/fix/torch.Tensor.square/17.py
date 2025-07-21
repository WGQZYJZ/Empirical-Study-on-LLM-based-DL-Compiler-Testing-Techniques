'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.square\ntorch.Tensor.square(_input_tensor)\n'
import torch
_input_tensor = torch.rand(3, 3)
_output_tensor = torch.Tensor.square(_input_tensor)
print(_output_tensor)
_output_tensor = torch.Tensor.sum(_input_tensor, dim=0)
print(_output_tensor)