import torch
from torch import nn
from torch.autograd import Variable
x = Variable(torch.ones(1, 1, 1, 1))
y = torch.nn.functional.feature_alpha_dropout(x, p=0.5)
y = torch.nn.functional.feature_alpha_dropout(x, p=0.5, training=True)