import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3)
storage = torch.ShortStorage(2)
storage.resize_(3)