'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.expm1_\ntorch.Tensor.expm1_(_input_tensor)\n'
import torch
from torch.autograd import Variable
_input_tensor = Variable(torch.randn(1, 3))
_out_tensor = torch.Tensor.expm1_(_input_tensor)
print(_out_tensor)