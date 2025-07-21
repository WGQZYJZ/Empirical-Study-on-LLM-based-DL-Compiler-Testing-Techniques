'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_\ntorch.Tensor.scatter_(_input_tensor, dim, index, src, reduce=None)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], dtype=torch.float32)
index = torch.tensor([[0, 0], [1, 1], [2, 2], [3, 3]], dtype=torch.int64)
src = torch.tensor([[10, 10], [20, 20], [30, 30], [40, 40]], dtype=torch.float32)
print('input_tensor: ', input_tensor)
print('index: ', index)
print('src: ', src)
print('Task 3: Call the API torch.Tensor.scatter_')
output_tensor = torch.Tensor.scatter_(input_tensor, dim=0, index=index, src=src)