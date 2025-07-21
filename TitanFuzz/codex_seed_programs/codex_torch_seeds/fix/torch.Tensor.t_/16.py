'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.t_\ntorch.Tensor.t_(_input_tensor)\n'
import torch
_input_tensor = torch.randn(3, 5)
_output_tensor = torch.Tensor.t_(_input_tensor)
print(_input_tensor)
print(_output_tensor)
_input_tensor = torch.randn(3, 5)
_output_tensor = torch.t(_input_tensor)
print(_input_tensor)
print(_output_tensor)
_input_tensor = torch.randn(3, 5)
_output_tensor = _input_tensor.t()
print(_input_tensor)
print(_output_tensor)