'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.outer\ntorch.Tensor.outer(_input_tensor, vec2)\n'
import torch
input_tensor = torch.randn(1, 3)
vec2 = torch.randn(3)
output_tensor = torch.Tensor.outer(input_tensor, vec2)
print(output_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_select\ntorch.Tensor.index_select(_input_tensor, dim, index)\n'
import torch
input_tensor = torch.randn(1, 3)
index = torch.LongTensor([0, 2])
output_tensor = torch.Tensor.index_select(input_tensor, 1, index)
print(output_tensor)