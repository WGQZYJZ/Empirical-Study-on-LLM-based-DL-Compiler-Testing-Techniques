import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3)
output = torch.clone(input_data)
input_data = torch.randn(2, 3, 4)
output = torch.clone(input_data)