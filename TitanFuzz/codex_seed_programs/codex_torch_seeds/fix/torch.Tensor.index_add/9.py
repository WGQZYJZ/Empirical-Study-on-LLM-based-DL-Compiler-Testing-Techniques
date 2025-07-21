'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_add\ntorch.Tensor.index_add(_input_tensor, dim, index, tensor2)\n'
import torch
input_tensor = torch.randn(3, 5)
index = torch.tensor([0, 2, 4])
updates = torch.tensor([1, 2, 3])
print(input_tensor)
print(input_tensor.index_add(0, index, updates))
print(input_tensor)