'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lgamma\ntorch.Tensor.lgamma(_input_tensor)\n'
import torch
from torch.autograd import Variable
input_tensor = Variable(torch.randn(3, 3))
output = torch.Tensor.lgamma(input_tensor)
print('input tensor = ', input_tensor)
print('output = ', output)