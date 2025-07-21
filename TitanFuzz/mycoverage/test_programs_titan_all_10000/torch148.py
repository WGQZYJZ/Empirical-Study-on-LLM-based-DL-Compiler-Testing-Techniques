import torch
from torch import nn
from torch.autograd import Variable
data = torch.rand(1000, 1000)
torch.set_num_threads(8)