import torch
from torch import nn
from torch.autograd import Variable
x1 = Variable(torch.randn(5, 3))
x2 = Variable(torch.randn(5, 3))
cos_sim = torch.nn.functional.cosine_similarity(x1, x2, dim=1, eps=1e-08)