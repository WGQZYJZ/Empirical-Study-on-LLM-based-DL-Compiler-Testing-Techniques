import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.rand(3, 3)
torch.polygamma(1, input_data)