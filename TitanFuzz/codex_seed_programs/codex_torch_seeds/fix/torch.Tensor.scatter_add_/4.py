'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_add_\ntorch.Tensor.scatter_add_(_input_tensor, dim, index, src)\n'
import torch
import torch
input_tensor = torch.randn(3, 4)
index = torch.tensor([1, 2, 0])
src = torch.tensor([2, 3, 4])
torch.Tensor.scatter_add_(input_tensor, dim=0, index=index, src=src)
print(input_tensor)