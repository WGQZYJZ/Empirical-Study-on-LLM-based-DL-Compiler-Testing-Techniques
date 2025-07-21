import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 5, 5, 5)
output = torch.nn.MaxPool3d(kernel_size=(1, 2, 2), stride=(1, 2, 2), padding=(0, 0, 0))(input)