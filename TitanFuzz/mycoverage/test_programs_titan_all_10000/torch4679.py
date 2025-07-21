import torch
from torch import nn
from torch.autograd import Variable
batch_size = 4
num_features = 3
height = 5
width = 5
in_channels = 3
x = torch.randn(batch_size, num_features, height, width, in_channels)
norm = torch.nn.LazyInstanceNorm3d(num_features)
x_norm = norm(x)
batch_size = 4
num_features = 3
height = 5
width = 5
in_channels = 3