'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_add_\ntorch.Tensor.scatter_add_(_input_tensor, dim, index, src)\n'
import torch
import torch
input_tensor = torch.zeros(3, 5)
index = torch.tensor([[4, 5, 4, 1], [3, 3, 2, 3]])
src = torch.tensor([[1, 0], [1, 1], [1, 0], [1, 1]])
output_tensor = torch.zeros(3, 5)
output_tensor.scatter_add_(dim=1, index=index, src=src)
print(output_tensor)