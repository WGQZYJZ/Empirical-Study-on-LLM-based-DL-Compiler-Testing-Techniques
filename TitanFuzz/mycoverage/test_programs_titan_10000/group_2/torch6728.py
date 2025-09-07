import torch
from torch import nn
from torch.autograd import Variable

data = torch.rand(100, 100)
num_interop_threads = torch.get_num_interop_threads()