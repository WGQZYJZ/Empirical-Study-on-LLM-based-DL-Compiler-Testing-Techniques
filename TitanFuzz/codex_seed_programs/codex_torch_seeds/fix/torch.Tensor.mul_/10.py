'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mul_\ntorch.Tensor.mul_(_input_tensor, value)\n'
import torch
_input_tensor = torch.rand(10, 10)
_result = torch.Tensor.mul_(_input_tensor, 2)
print(_result)