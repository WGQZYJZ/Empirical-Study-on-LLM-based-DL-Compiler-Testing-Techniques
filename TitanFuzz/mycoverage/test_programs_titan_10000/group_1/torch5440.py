import torch
from torch import nn
from torch.autograd import Variable

tensor = torch.randn(2, 3, 4)
tensor = torch.moveaxis(tensor, 0, (- 1))