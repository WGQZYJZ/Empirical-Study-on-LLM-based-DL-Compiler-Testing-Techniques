import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, 3)
model = torch.nn.Sequential(torch.nn.Linear(3, 2), torch.nn.ReLU(), torch.nn.Linear(2, 1), torch.nn.ReLU())