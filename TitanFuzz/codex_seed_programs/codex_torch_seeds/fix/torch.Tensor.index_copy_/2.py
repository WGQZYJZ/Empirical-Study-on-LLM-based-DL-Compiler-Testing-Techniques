'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_copy_\ntorch.Tensor.index_copy_(_input_tensor, dim, index, tensor)\n'
import torch
input_tensor = torch.rand(2, 3)
print(input_tensor)
dim = 0
index = torch.LongTensor([0, 2])
tensor = torch.rand(2, 3)
input_tensor.index_copy_(dim, index, tensor)
print(input_tensor)