'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ceil\ntorch.Tensor.ceil(_input_tensor)\n'
import torch
input_tensor = torch.randn(4, 4)
print('input_tensor:', input_tensor)
output_tensor = torch.Tensor.ceil(input_tensor)
print('output_tensor:', output_tensor)