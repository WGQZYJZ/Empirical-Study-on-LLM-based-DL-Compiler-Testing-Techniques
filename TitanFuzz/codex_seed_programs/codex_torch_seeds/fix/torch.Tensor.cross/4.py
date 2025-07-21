'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cross\ntorch.Tensor.cross(_input_tensor, other, dim=-1)\n'
import torch
from torch.autograd import Variable
input_tensor = Variable(torch.randn(3, 4))
other = Variable(torch.randn(3, 4))
output_tensor = torch.Tensor.cross(input_tensor, other, dim=(- 1))
print('input_tensor = \n', input_tensor)
print('other = \n', other)
print('output_tensor = \n', output_tensor)