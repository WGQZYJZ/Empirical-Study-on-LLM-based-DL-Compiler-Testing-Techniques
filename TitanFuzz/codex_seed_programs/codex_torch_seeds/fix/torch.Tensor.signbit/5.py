'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.signbit\ntorch.Tensor.signbit(_input_tensor)\n'
import torch
_input_tensor = torch.randn(3, 3)
_output_tensor = _input_tensor.signbit()
print(_output_tensor)