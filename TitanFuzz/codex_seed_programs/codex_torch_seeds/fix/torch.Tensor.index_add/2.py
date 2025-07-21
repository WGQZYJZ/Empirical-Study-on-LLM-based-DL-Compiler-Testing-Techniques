'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_add\ntorch.Tensor.index_add(_input_tensor, dim, index, tensor2)\n'
import torch
input_tensor = torch.randn(3, 3)
print(input_tensor)
index = torch.tensor([1, 0, 2, 0, 2, 1])
tensor2 = torch.tensor([1, 1, 1, 1, 1, 1])
print(torch.Tensor.index_add(input_tensor, 0, index, tensor2))