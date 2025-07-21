'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_add_\ntorch.Tensor.scatter_add_(_input_tensor, dim, index, src)\n'
import torch
input_tensor = torch.randn(4, 5)
print('input_tensor:', input_tensor)
index = torch.tensor([0, 2, 3, 1])
src = torch.tensor([5, 6, 7, 8])
output_tensor = torch.zeros_like(input_tensor)
output_tensor.scatter_add_(dim=0, index=index, src=src)
print('output_tensor:', output_tensor)