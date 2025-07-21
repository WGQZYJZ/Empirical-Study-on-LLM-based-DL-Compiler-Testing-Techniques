'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.trunc_\ntorch.Tensor.trunc_(_input_tensor)\n'
import torch
_input_tensor = torch.randn(4, 4)
_output_tensor = _input_tensor.trunc_()
print(_input_tensor)
print(_output_tensor)