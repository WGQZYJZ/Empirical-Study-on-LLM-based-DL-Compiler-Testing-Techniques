import torch
from torch import nn
from torch.autograd import Variable
input_size = 10
output_size = 20
tensor = torch.zeros(input_size, output_size)
torch.nn.init.kaiming_uniform_(tensor, a=0, mode='fan_in', nonlinearity='leaky_relu')