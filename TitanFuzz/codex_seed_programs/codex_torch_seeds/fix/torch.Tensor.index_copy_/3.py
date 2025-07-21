'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_copy_\ntorch.Tensor.index_copy_(_input_tensor, dim, index, tensor)\n'
import torch
import torch
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
torch.Tensor.index_copy_(input_tensor, 0, torch.LongTensor([0, 2]), torch.Tensor([[11, 12, 13], [14, 15, 16]]))
print(input_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_fill_\ntorch.Tensor.index_fill_(_input_tensor, dim, index, value)\n'
import torch
import torch