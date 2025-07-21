import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(2, 2)
result = torch.true_divide(input_data, 2)