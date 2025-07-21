import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(3, 3)
output = torch.cholesky_inverse(input_data)
input_data = torch.rand(3, 3)
output = torch.cholesky_inverse(input_data, upper=True)