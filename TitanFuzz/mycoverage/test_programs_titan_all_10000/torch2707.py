import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3)
size = torch.LongStorage(input_data.size())