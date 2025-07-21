'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.igammac_\ntorch.Tensor.igammac_(_input_tensor, other)\n'
import torch
from torch.autograd import Variable
dtype = torch.FloatTensor
_input_tensor = Variable(torch.randn(4, 4).type(dtype))
other = Variable(torch.randn(4, 4).type(dtype))
print(torch.Tensor.igammac_(_input_tensor, other))