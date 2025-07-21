'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sgn\ntorch.Tensor.sgn(_input_tensor)\n'
import torch
_input_tensor = torch.randn(1, 3, 3)
_output_tensor = _input_tensor.sgn()
print(_output_tensor)