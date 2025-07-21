'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mul_\ntorch.Tensor.mul_(_input_tensor, value)\n'
import torch
_input_tensor = torch.randn(2, 3)
value = torch.randn(1, 3)
_output_tensor = torch.Tensor.mul_(_input_tensor, value)
print(_output_tensor)