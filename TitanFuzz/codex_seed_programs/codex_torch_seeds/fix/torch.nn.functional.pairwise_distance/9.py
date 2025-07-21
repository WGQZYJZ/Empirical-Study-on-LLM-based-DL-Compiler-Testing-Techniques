'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.pairwise_distance\ntorch.nn.functional.pairwise_distance(x1, x2, p=2.0, eps=1e-06, keepdim=False)\n'
import torch
import torch.nn as nn
from torch.autograd import Variable
x1 = Variable(torch.randn(10, 3))
x2 = Variable(torch.randn(10, 3))
dist = nn.functional.pairwise_distance(x1, x2)
print(dist)