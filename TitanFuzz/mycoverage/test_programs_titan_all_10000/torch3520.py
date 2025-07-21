import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 3, 4, 4)
output = torch.nn.functional.tanhshrink(input_data)