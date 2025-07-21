'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.div\ntorch.Tensor.div(_input_tensor, value, *, rounding_mode=None)\n'
import torch
input_tensor = torch.randn(2, 3)
print(input_tensor)
print(input_tensor.div(2))
print(input_tensor.div(2.0))
print(input_tensor.div(2.0, out=input_tensor))
print(input_tensor)
print(input_tensor.div(2, out=input_tensor))
print(input_tensor)