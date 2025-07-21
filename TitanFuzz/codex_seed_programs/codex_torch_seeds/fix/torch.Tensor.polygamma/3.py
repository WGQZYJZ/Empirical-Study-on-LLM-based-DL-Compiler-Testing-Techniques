'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.polygamma\ntorch.Tensor.polygamma(_input_tensor, n)\n'
import torch
import torch
input_tensor = torch.rand(4, 4)
output_tensor = input_tensor.polygamma(7)
print('input_tensor:', input_tensor)
print('output_tensor:', output_tensor)