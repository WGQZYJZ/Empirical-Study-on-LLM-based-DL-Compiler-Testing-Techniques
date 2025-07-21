'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ldexp\ntorch.Tensor.ldexp(_input_tensor, other)\n'
import torch
_input_tensor = torch.rand(10, 10)
output = torch.Tensor.ldexp(_input_tensor, 2)
print('Output: ', output)