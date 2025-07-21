'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_copy_\ntorch.Tensor.index_copy_(_input_tensor, dim, index, tensor)\n'
import torch
input_tensor = torch.randn(2, 3)
index = torch.tensor([0, 2])
tensor = torch.tensor([[1, 1, 1], [2, 2, 2]])
torch.Tensor.index_copy_(input_tensor, 0, index, tensor)
print(input_tensor)