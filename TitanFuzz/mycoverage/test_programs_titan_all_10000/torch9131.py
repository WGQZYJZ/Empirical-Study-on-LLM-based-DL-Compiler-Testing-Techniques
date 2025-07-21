import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([1, 2, 3])
torch.special.entr(x)
torch.special.entr(x, out=torch.empty(x.size()))