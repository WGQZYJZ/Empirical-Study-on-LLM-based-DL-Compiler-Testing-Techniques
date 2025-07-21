import torch
from torch import nn
from torch.autograd import Variable
data = torch.tensor([[True, True, True, True], [True, True, True, True]])
torch.all(data)
torch.all(data, dim=0)
torch.all(data, dim=0, keepdim=True)