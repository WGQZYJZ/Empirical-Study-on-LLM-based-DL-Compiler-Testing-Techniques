import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.arange(1, 11)
result = torch.narrow(input_data, 0, 0, 4)