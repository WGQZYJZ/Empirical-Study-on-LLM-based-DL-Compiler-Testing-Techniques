import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([1, 2, 3])
y = torch.tensor([1.0, 2.0, 3.0])
torch.promote_types(x.dtype, y.dtype)