'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_copy\ntorch.Tensor.index_copy(_input_tensor, dim, index, tensor2)\n'
import torch
input_tensor = torch.rand(5, 3)
print('input_tensor: ', input_tensor)
index_tensor = torch.LongTensor([0, 2])
print('index_tensor: ', index_tensor)
copy_tensor = torch.rand(2, 3)
print('copy_tensor: ', copy_tensor)
output_tensor = torch.Tensor.index_copy(input_tensor, 0, index_tensor, copy_tensor)
print('output_tensor: ', output_tensor)