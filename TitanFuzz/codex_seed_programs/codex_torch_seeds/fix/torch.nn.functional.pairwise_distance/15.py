'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.pairwise_distance\ntorch.nn.functional.pairwise_distance(x1, x2, p=2.0, eps=1e-06, keepdim=False)\n'
import torch
from torch.autograd import Variable
import numpy as np
x1 = Variable(torch.randn(3, 4))
x2 = Variable(torch.randn(3, 4))
d = torch.nn.functional.pairwise_distance(x1, x2, p=2.0, eps=1e-06, keepdim=False)
print(d)