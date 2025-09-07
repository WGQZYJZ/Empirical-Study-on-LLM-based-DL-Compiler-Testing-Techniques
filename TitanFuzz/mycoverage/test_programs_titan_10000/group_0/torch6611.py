import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.randn(5)
softplus = torch.nn.Softplus()
output_data = softplus(input_data)