'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_add\ntorch.Tensor.scatter_add(_input_tensor, dim, index, src)\n'
import torch
input_tensor = torch.rand(3, 4)
index = torch.LongTensor([[0, 1], [2, 0]])
src = torch.rand(2, 2)
output_tensor = torch.Tensor.scatter_add(input_tensor, 0, index, src)
print(output_tensor)