'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_\ntorch.Tensor.scatter_(_input_tensor, dim, index, src, reduce=None)\n'
import torch
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(torch.Tensor.scatter_(input_tensor, 0, torch.Tensor([[0, 0, 0], [1, 1, 1], [2, 2, 2]]), torch.Tensor([[1, 1, 1], [2, 2, 2], [3, 3, 3]])))
print(torch.Tensor.scatter_(input_tensor, 1, torch.Tensor([[0, 0, 0], [1, 1, 1], [2, 2, 2]]), torch.Tensor([[1, 1, 1], [2, 2, 2], [3, 3, 3]])))