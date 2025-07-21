import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([(- 1.0), (- 0.5), 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5])
boundaries = torch.tensor([0.0, 1.0, 2.0])
output = torch.bucketize(input, boundaries)