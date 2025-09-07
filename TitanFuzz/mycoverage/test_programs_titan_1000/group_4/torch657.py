import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(100, 100)
x = Variable(x)
torch.nn.FeatureAlphaDropout(p=0.5, inplace=False)
F.dropout(x, p=0.5, training=True, inplace=False)
x = torch.randn(100, 100)