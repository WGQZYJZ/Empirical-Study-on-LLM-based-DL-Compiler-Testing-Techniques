import torch
from torch import nn
from torch.autograd import Variable

x = torch.tensor([1, 2, 3])
torch.set_default_dtype(torch.float32)