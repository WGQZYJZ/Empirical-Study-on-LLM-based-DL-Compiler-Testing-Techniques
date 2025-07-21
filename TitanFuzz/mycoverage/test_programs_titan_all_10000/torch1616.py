import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3, 4)
input2 = torch.randn(2, 3, 4)
input3 = torch.randn(2, 3, 4)
output = torch.Tensor.ormqr(input_tensor, input2, input3, left=True, transpose=False)