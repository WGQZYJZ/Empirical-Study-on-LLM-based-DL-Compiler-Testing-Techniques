'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.multiply\ntorch.Tensor.multiply(_input_tensor, value)\n'
import torch
_input_tensor = torch.rand(2, 3, 4)
_input_value = 2
_output_tensor = torch.Tensor.multiply(_input_tensor, _input_value)
print(_output_tensor)