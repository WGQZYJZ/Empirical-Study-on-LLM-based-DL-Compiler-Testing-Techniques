'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_add_\ntorch.Tensor.index_add_(_input_tensor, dim, index, tensor, *, alpha=1)\n'
import torch
input_tensor = torch.randn(3, 3)
index_tensor = torch.tensor([0, 2, 1])
update_tensor = torch.tensor([1, 2, 3])
output_tensor = torch.Tensor.index_add_(input_tensor, 0, index_tensor, update_tensor)
print(output_tensor)