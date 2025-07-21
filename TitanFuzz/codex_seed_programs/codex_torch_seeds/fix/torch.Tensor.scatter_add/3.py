'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_add\ntorch.Tensor.scatter_add(_input_tensor, dim, index, src)\n'
import torch
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float32)
index = torch.tensor([0, 2, 1, 0], dtype=torch.int64)
src = torch.tensor([[10, 20, 30], [40, 50, 60], [70, 80, 90], [100, 200, 300]], dtype=torch.float32)
dim = 0
output_tensor = torch.Tensor.scatter_add(input_tensor, dim, index, src)
print('input_tensor: ', input_tensor)
print('index: ', index)
print('src: ', src)
print('dim: ', dim)
print('output_tensor: ', output_tensor)