import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 4, 4, 4)
torch.nn.AdaptiveMaxPool3d(output_size=(2, 2, 2))(input)