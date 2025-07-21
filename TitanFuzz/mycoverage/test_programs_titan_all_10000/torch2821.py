import torch
from torch import nn
from torch.autograd import Variable
data = torch.tensor([(- 1), (- 2), (- 3), (- 4)])
torch.Tensor.neg_(data)