'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_add_\ntorch.Tensor.scatter_add_(_input_tensor, dim, index, src)\n'
import torch
input_tensor = torch.randn(3, 4)
index = torch.tensor([1, 2, 0, 1, 2, 2])
src = torch.tensor([3, 2, 1, 2, 1, 2])
input_tensor.scatter_add_(0, index, src)
print(input_tensor)