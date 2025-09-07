import torch
from torch import nn
from torch.autograd import Variable

data = list(range(10))
storage = torch.ByteStorage(data)