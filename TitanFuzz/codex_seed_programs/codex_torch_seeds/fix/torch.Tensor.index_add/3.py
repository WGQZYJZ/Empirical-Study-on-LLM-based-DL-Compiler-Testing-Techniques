'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_add\ntorch.Tensor.index_add(_input_tensor, dim, index, tensor2)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
index = torch.tensor([0, 1, 2])
tensor2 = torch.tensor([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
torch.Tensor.index_add(input_tensor, 0, index, tensor2)
print('input_tensor:', input_tensor)
print('index:', index)
print('tensor2:', tensor2)