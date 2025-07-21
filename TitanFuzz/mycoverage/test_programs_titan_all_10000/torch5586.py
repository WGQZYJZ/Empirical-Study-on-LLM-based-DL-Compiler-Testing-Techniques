import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.ones(5)
output = torch.ones(5, out=input_data)