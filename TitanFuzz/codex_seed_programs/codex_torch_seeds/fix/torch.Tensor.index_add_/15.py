'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_add_\ntorch.Tensor.index_add_(_input_tensor, dim, index, tensor, *, alpha=1)\n'
import torch
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
index = torch.tensor([0, 1, 0], dtype=torch.int64)
tensor = torch.tensor([[10, 20, 30], [40, 50, 60], [100, 200, 300]], dtype=torch.float32)
output_tensor = torch.Tensor.index_add_(input_tensor, dim=0, index=index, tensor=tensor)
print('output_tensor:', output_tensor)