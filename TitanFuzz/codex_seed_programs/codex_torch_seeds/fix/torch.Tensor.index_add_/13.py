'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_add_\ntorch.Tensor.index_add_(_input_tensor, dim, index, tensor, *, alpha=1)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
index = torch.tensor([0, 2, 1])
tensor = torch.tensor([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
output_tensor = torch.Tensor.index_add_(input_tensor, dim=0, index=index, tensor=tensor)
print(output_tensor)