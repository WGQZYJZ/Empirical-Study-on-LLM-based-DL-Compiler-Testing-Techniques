import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1, 3, 5, 5, 5)
y = torch.randn(1, 3, 5, 5, 5)
z = torch.nn.AdaptiveAvgPool3d(output_size=2)