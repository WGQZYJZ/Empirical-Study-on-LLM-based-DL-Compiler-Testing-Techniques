'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.div_\ntorch.Tensor.div_(_input_tensor, value, *, rounding_mode=None)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input_tensor = Variable(torch.randn(2, 3))
print('input_tensor: ', input_tensor)
input_tensor.div_(2)
print('input_tensor.div_(2): ', input_tensor)
input_tensor.div_(2, out=input_tensor)
print('input_tensor.div_(2, out=input_tensor): ', input_tensor)