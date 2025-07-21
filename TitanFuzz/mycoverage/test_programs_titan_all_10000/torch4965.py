import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor(data=[2.0, 3.0], requires_grad=True)
optimizer = torch.optim.RMSprop([x], lr=0.01)