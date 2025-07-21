'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dist\ntorch.Tensor.dist(_input_tensor, other, p=2)\n'
import torch
from torch.autograd import Variable
input_tensor = torch.ones(2, 3)
print('input_tensor: ', input_tensor)
other = (torch.ones(2, 3) * 2)
print('other: ', other)
result = input_tensor.dist(other)
print('result: ', result)