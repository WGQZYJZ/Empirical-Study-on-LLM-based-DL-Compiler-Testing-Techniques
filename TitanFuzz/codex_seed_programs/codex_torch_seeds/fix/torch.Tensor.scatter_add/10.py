'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_add\ntorch.Tensor.scatter_add(_input_tensor, dim, index, src)\n'
import torch
input_tensor = torch.rand(4, 4)
print(input_tensor)
dim = 0
index = torch.tensor([1, 2, 3])
src = torch.tensor([1, 2, 3])
output_tensor = torch.Tensor.scatter_add(input_tensor, dim, index, src)
print(output_tensor)
print('Done')