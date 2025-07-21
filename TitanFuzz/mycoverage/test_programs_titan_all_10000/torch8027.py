import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3)
log_sigmoid = torch.nn.LogSigmoid()
output = log_sigmoid(input_data)