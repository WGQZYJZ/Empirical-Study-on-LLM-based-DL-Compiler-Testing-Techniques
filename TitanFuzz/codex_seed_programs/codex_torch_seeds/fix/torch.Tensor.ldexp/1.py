'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ldexp\ntorch.Tensor.ldexp(_input_tensor, other)\n'
import torch
input_tensor = torch.randn(4, 4)
print('Input Tensor: ', input_tensor)
print('Output Tensor: ', input_tensor.ldexp(2))