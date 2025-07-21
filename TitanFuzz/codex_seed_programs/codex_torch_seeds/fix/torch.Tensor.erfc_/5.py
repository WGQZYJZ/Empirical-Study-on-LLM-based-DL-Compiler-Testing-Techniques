'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.erfc_\ntorch.Tensor.erfc_(_input_tensor)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input_tensor = Variable(torch.randn(3, 3))
output_tensor = torch.Tensor.erfc_(input_tensor)
print('input_tensor:', input_tensor)
print('output_tensor:', output_tensor)