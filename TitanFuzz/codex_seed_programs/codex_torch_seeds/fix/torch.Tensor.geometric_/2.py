'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.geometric_\ntorch.Tensor.geometric_(_input_tensor, p, *, generator=None)\n'
import torch
input_tensor = torch.rand(10)
p = 0.5
output_tensor = torch.Tensor.geometric_(input_tensor, p)
print('input_tensor: ', input_tensor)
print('output_tensor: ', output_tensor)