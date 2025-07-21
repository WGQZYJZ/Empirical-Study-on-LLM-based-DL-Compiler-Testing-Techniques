'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_add_\ntorch.Tensor.scatter_add_(_input_tensor, dim, index, src)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
print(input_tensor)
print(input_tensor.shape)
index = torch.tensor([[0, 1, 2, 0], [2, 0, 0, 1]])
src = torch.randn(2, 4)
print(src)
print(src.shape)
input_tensor.scatter_add_(dim=0, index=index, src=src)
print(input_tensor)