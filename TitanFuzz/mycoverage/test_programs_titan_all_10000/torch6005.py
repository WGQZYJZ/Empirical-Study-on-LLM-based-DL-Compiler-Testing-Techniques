import torch
from torch import nn
from torch.autograd import Variable
data = torch.tensor([[1, 2], [3, 4]])
indices = torch.tensor([[0, 1], [1, 0]])
torch.gather(data, dim=0, index=indices)