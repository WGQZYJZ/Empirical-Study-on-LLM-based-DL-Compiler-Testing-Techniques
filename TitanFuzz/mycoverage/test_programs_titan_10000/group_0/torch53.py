import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.arange(0, 100)
sampler = torch.utils.data.Sampler(input_data)