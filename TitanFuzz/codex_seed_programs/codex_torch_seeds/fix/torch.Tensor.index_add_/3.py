'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_add_\ntorch.Tensor.index_add_(_input_tensor, dim, index, tensor, *, alpha=1)\n'
import torch
import torch
input_tensor = torch.tensor([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]])
print(input_tensor)
result_tensor = torch.Tensor.index_add_(input_tensor, 0, torch.tensor([0, 1]), torch.tensor([[1, 1, 1], [1, 1, 1]]))
print(result_tensor)