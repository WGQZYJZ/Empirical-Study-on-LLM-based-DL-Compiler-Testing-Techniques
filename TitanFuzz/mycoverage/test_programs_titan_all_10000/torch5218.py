import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.arange(0, 10)
input_data = torch.arange(0, 10, 2)
input_data = torch.arange(0, 10, 2, dtype=torch.float)