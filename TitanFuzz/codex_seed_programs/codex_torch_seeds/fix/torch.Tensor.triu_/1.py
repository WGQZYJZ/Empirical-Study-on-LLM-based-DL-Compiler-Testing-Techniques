'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.triu_\ntorch.Tensor.triu_(_input_tensor, diagonal=0)\n'
import torch
input_tensor = torch.randn(4, 4)
output_tensor = input_tensor.triu_(diagonal=1)
print('input_tensor:', input_tensor)
print('output_tensor:', output_tensor)