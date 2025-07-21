import torch
from torch import nn
from torch.autograd import Variable
shape1 = torch.Size([2, 3, 4])
shape2 = torch.Size([3, 4])
result = torch.broadcast_shapes(shape1, shape2)