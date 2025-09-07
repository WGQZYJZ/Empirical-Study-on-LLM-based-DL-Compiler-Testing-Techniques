import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(1, 5)
torch.nn.FeatureAlphaDropout(p=0.5, inplace=False)