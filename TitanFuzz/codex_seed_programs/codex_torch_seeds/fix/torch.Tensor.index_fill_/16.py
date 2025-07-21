'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_fill_\ntorch.Tensor.index_fill_(_input_tensor, dim, index, value)\n'
import torch
import torch
input_tensor = torch.randn(3, 3)
print(input_tensor)
input_tensor.index_fill_(1, torch.LongTensor([0, 2]), 0)
print(input_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_select_\ntorch.Tensor.index_select_(_input_tensor, dim, index)\n'
import torch
import torch
input_tensor = torch.randn(3, 3)
print(input_tensor)
result = input_tensor.index_select(1, torch.LongTensor([0, 2]))
print(result)