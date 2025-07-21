import torch
from torch import nn
from torch.autograd import Variable
x1 = torch.randn(5, 5)
x2 = torch.randn(5, 5)
torch.nn.functional.cosine_similarity(x1, x2, dim=1, eps=1e-08)