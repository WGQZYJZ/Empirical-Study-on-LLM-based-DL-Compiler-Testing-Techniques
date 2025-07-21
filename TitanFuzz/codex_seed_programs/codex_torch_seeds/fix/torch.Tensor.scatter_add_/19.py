'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_add_\ntorch.Tensor.scatter_add_(_input_tensor, dim, index, src)\n'
import torch
import torch
input_tensor = torch.rand(2, 3)
dim = 1
index = torch.tensor([0, 1, 1], dtype=torch.long)
src = torch.tensor([1, 2, 3], dtype=torch.float)
torch.Tensor.scatter_add_(input_tensor, dim, index, src)
print(input_tensor)