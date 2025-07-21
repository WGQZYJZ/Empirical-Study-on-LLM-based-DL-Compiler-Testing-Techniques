import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 2, 3, 4)
log_sigmoid = torch.nn.LogSigmoid()
output_data = log_sigmoid(input_data)