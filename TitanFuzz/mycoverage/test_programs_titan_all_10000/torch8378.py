import torch
from torch import nn
from torch.autograd import Variable
data = torch.rand(2, 3)
torch.set_num_threads(4)