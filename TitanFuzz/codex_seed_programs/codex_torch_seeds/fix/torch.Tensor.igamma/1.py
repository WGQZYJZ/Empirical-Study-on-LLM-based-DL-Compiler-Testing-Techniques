'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.igamma\ntorch.Tensor.igamma(_input_tensor, other)\n'
import torch
'\nTask 1: import PyTorch\n'
import torch
'\nTask 2: Generate input data\n'
input_tensor = torch.rand(3, 4, 5)
'\nTask 3: Call the API torch.Tensor.igamma\ntorch.Tensor.igamma(_input_tensor, other)\n'
output_tensor = torch.Tensor.igamma(input_tensor, other=2)
print('input_tensor: ', input_tensor)
print('output_tensor: ', output_tensor)