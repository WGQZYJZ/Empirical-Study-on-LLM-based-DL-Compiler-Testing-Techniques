'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter\ntorch.Tensor.scatter(_input_tensor, dim, index, src)\n'
import torch
input_tensor = torch.rand(3, 5)
print('input_tensor: ', input_tensor)
index = torch.tensor([[4, 5, 4, 1], [3, 3, 2, 0]])
src = torch.tensor([[1, 0, 1, 0], [1, 1, 0, 0]])
output_tensor = torch.Tensor.scatter(input_tensor, dim=0, index=index, src=src)
print('output_tensor: ', output_tensor)