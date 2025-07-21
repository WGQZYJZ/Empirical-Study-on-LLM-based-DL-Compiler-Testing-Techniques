import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randperm(10)
output_data = torch.randperm(input_data.size(0), out=None)