import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(1000, 1000)
torch.set_num_interop_threads(4)