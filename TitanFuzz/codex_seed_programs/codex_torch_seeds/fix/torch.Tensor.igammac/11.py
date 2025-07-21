'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.igammac\ntorch.Tensor.igammac(_input_tensor, other)\n'
import torch
import torch
_input_tensor = torch.randn(4, 4)
_output_tensor = _input_tensor.igammac(3)
print(_output_tensor)