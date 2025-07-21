import torch
from torch import nn
from torch.autograd import Variable
tensor = torch.Tensor(3, 3)
tensor.fill_(0)
torch.nn.init.orthogonal_(tensor, gain=1)