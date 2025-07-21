'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_add\ntorch.Tensor.index_add(_input_tensor, dim, index, tensor2)\n'
import torch
input_tensor = torch.randn(4, 3)
index = torch.tensor([0, 2])
tensor2 = torch.tensor([1, 2])
print(input_tensor)
print(input_tensor.index_add(0, index, tensor2))