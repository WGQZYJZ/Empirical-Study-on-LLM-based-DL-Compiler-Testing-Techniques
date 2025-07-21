import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([[1, 2, 3], [4, 5, 6]])
y = torch.nn.functional.pad(x, (1, 2), mode='constant', value=0)