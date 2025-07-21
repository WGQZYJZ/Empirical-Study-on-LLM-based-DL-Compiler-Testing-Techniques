'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_\ntorch.Tensor.scatter_(_input_tensor, dim, index, src, reduce=None)\n'
import torch
input_tensor = torch.rand(4, 3)
print('Input tensor: \n{}'.format(input_tensor))
index = torch.tensor([[0, 1, 2, 0], [2, 0, 0, 1]])
print('Index: \n{}'.format(index))
src = torch.tensor([3.1415, 2.7182])
print('Source: \n{}'.format(src))
output_tensor = torch.Tensor.scatter_(input_tensor, 0, index, src)
print('Output tensor: \n{}'.format(output_tensor))