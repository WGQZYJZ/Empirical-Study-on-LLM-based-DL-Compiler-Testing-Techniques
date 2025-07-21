'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ldexp\ntorch.Tensor.ldexp(_input_tensor, other)\n'
import torch
input_tensor = torch.randn(4, 4)
output_tensor = torch.Tensor.ldexp(input_tensor, 2)
print('input tensor:', input_tensor)
print('output tensor:', output_tensor)