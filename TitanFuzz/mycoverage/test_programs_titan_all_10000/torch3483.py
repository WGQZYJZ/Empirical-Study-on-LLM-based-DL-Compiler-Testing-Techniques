import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(3, 3)
input_data_type = torch.jit.annotate(input_data, input_data)