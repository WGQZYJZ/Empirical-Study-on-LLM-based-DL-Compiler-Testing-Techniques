import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(4, 3)
torch.nanquantile(input, q=0.5, dim=0, keepdim=False, out=None)
q = torch.tensor([0.25, 0.5, 0.75])
torch.nanquantile(input, q=q, dim=0, keepdim=False, out=None)
q = torch.tensor([0.25, 0.5, 0.75])
torch.nanquantile(input, q=q, dim=1, keepdim=False, out=None)