'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.hypot_\ntorch.Tensor.hypot_(_input_tensor, other)\n'
import torch
import torch
input_tensor = torch.Tensor([[2, 3], [4, 5]])
other = torch.Tensor([[1, 2], [3, 4]])
result = torch.Tensor.hypot_(input_tensor, other)
print('result:', result)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_add_\ntorch.Tensor.index_add_(dim, index, tensor)\n'
import torch
import torch
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
dim = 1
index = torch.LongTensor([0, 1, 1])