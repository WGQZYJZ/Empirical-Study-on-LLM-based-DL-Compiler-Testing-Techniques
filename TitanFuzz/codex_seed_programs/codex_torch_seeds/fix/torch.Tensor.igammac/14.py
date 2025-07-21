'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.igammac\ntorch.Tensor.igammac(_input_tensor, other)\n'
import torch
_input_tensor = torch.rand(1, 1)
other = torch.rand(1, 1)
_output_tensor = _input_tensor.igammac(other)
print(_input_tensor)
print(_output_tensor)