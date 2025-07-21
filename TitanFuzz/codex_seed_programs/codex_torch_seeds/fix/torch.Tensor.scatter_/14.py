'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_\ntorch.Tensor.scatter_(_input_tensor, dim, index, src, reduce=None)\n'
import torch
input_tensor = torch.randn(3, 5)
print('Input tensor: ', input_tensor)
index = torch.tensor([1, 2, 0])
src = torch.tensor([1, 2, 3])
output_tensor = input_tensor.scatter_(0, index, src)
print('Output tensor: ', output_tensor)