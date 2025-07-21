'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_add_\ntorch.Tensor.index_add_(_input_tensor, dim, index, tensor, *, alpha=1)\n'
import torch
import torch
input_tensor = torch.randn(3, 4)
index = torch.tensor([0, 2])
tensor = torch.tensor([[1, 1, 1, 1], [1, 1, 1, 1]])
output_tensor = torch.Tensor.index_add_(input_tensor, dim=0, index=index, tensor=tensor)
print('The input tensor is:', input_tensor)
print('The output tensor is:', output_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_copy_\ntorch.Tensor.index_copy_(input_tensor, dim, index, tensor)\n'
import torch
import torch