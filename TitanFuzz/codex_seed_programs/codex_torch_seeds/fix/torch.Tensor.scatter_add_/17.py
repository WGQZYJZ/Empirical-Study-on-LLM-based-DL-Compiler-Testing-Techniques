'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_add_\ntorch.Tensor.scatter_add_(_input_tensor, dim, index, src)\n'
import torch
input_tensor = torch.ones(4, 4)
index_tensor = torch.tensor([[2, 3], [1, 0], [0, 1], [3, 2]])
source_tensor = torch.tensor([[1, 2], [3, 4], [5, 6], [7, 8]])
result = torch.Tensor.scatter_add_(input_tensor, dim=1, index=index_tensor, src=source_tensor)
print(result)