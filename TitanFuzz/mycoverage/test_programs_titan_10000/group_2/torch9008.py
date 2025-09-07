import torch
from torch import nn
from torch.autograd import Variable

a = torch.tensor([[1, 2, 3], [4, 5, 6]])
b = torch.tensor([[1, 2, 3], [4, 5, 6]])
torch.is_warn_always_enabled()