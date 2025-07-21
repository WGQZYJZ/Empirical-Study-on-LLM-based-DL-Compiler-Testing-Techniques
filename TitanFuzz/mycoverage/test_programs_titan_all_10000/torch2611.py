import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3)
input_data_size = torch.LongStorage(input_data.size())