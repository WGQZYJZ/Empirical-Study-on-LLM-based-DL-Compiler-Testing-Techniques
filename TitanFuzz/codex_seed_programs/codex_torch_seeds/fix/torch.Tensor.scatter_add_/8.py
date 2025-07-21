'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_add_\ntorch.Tensor.scatter_add_(_input_tensor, dim, index, src)\n'
import torch
input_tensor = torch.randn(3, 4)
index = torch.tensor([0, 1, 2, 0])
src = torch.tensor([1, 2, 3, 4])
output_tensor = torch.Tensor.scatter_add_(input_tensor, dim=0, index=index, src=src)
print(output_tensor)