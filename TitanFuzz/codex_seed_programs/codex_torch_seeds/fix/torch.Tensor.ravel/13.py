'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ravel\ntorch.Tensor.ravel(_input_tensor)\n'
import torch
_input_tensor = torch.rand((2, 3, 4))
_output_tensor = _input_tensor.ravel()
print(_input_tensor)
print(_output_tensor)