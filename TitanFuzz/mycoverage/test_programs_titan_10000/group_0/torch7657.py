import torch
from torch import nn
from torch.autograd import Variable

data = torch.randn(10, dtype=torch.bfloat16)
storage = torch.BFloat16Storage()