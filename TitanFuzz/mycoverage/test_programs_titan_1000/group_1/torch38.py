import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(5, 5)
relu_output = torch.nn.functional.relu_(input)
relu_output = torch.nn.functional.relu_(input)