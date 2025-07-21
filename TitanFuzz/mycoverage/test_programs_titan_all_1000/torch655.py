import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([(- 1), (- 0.5), 0, 0.5, 1])
boundaries = torch.tensor([0])
torch.bucketize(input, boundaries, out_int32=False, right=False, out=None)