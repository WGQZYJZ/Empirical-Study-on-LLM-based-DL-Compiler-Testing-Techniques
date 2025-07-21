import torch
from torch import nn
from torch.autograd import Variable
in1_features = 2
in2_features = 3
out_features = 4
bilinear = torch.nn.Bilinear(in1_features, in2_features, out_features)
input1 = torch.randn(1, in1_features)