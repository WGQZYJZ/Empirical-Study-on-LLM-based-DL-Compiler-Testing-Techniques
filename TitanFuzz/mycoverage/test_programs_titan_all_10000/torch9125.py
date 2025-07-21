import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.randn(1, 2, 3))
output_data = torch.nn.functional.rrelu_(input_data, lower=(1.0 / 8), upper=(1.0 / 3), training=False)