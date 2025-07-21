'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.log1p\ntorch.Tensor.log1p(_input_tensor)\n'
import torch
input_tensor = torch.rand(10, 10)
output_tensor = torch.Tensor.log1p(input_tensor)
print('input_tensor:', input_tensor)
print('output_tensor:', output_tensor)