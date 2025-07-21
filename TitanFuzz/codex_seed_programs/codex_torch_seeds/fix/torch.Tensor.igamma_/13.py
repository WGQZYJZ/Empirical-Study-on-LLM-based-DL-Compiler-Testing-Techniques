'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.igamma_\ntorch.Tensor.igamma_(_input_tensor, other)\n'
import torch
input_tensor = torch.randn(4, 4)
other = torch.randn(4, 4)
output_tensor = torch.Tensor.igamma_(input_tensor, other)
print('input tensor:', input_tensor)
print('output tensor:', output_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_add_\ntorch.Tensor.index_add_(dim, index, tensor)\n'
import torch
input_tensor = torch.randn(4, 4)
dim = 1
index = torch.tensor([1, 3])
tensor = torch.randn(2, 4)