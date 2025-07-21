'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_add_\ntorch.Tensor.index_add_(_input_tensor, dim, index, tensor, *, alpha=1)\n'
import torch
input_tensor = torch.rand(3, 4, 5)
index = torch.tensor([[0, 1, 2, 3], [1, 2, 3, 0], [2, 3, 0, 1]])
tensor = torch.rand(3, 4)
input_tensor.index_add_(1, index, tensor)
print(input_tensor)