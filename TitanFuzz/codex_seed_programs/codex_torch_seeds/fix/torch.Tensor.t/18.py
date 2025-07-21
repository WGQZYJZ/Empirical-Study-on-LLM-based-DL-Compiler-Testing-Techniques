'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.t\ntorch.Tensor.t(_input_tensor)\n'
import torch
_input = torch.randn(2, 3)
_input_tensor = torch.randn(2, 3)
_output = _input.t()
print(_output)