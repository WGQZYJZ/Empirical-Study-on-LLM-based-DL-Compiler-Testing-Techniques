import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.FloatTensor([[1, 2, 3], [4, 5, 6]]))
target = Variable(torch.FloatTensor([[0, 1, 0], [1, 0, 1]]))
loss = torch.nn.functional.multilabel_soft_margin_loss(input, target)