import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([1.0, 2.0, 4.0, 8.0])
output = torch.log2(input_data)