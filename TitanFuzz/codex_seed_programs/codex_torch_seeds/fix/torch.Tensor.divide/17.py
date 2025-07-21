'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.divide\ntorch.Tensor.divide(_input_tensor, value, *, rounding_mode=None)\n'
import torch
_input_tensor = torch.randn(4, 4)
print(_input_tensor)
_divide_by_value = 10
_output_tensor = _input_tensor.divide(_divide_by_value)
print(_output_tensor)