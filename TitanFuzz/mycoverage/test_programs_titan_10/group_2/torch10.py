import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.Tensor([0.1, 0.2, 0.3, 0.4])
output = torch.atanh(input_data)