'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.round_\ntorch.Tensor.round_(_input_tensor)\n'
import torch
_input_tensor = torch.rand(5, 5)
_output_tensor = _input_tensor.round_()
print(_input_tensor)
print(_output_tensor)