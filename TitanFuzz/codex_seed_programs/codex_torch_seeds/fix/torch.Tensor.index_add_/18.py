'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_add_\ntorch.Tensor.index_add_(_input_tensor, dim, index, tensor, *, alpha=1)\n'
import torch
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
index = torch.tensor([[0, 1, 0], [1, 0, 1]])
tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
torch.Tensor.index_add_(input_tensor, dim=1, index=index, tensor=tensor)
print(input_tensor)