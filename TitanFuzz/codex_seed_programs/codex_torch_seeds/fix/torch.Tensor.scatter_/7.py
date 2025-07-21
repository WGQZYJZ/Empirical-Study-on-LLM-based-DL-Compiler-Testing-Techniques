'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_\ntorch.Tensor.scatter_(_input_tensor, dim, index, src, reduce=None)\n'
import torch
input_tensor = torch.randn(3, 4)
index = torch.tensor([[1, 2], [0, 2]])
src = torch.tensor([[1, 0], [1, 1]])
result = torch.Tensor.scatter_(input_tensor, dim=0, index=index, src=src)
print(result)