import torch
from torch import nn
from torch.autograd import Variable
input1 = Variable(torch.randn(3, 5), requires_grad=True)
input2 = Variable(torch.randn(3, 5), requires_grad=True)
target = Variable(torch.Tensor(3).random_(2))
loss = torch.nn.CosineEmbeddingLoss(margin=0.0, size_average=None, reduce=None, reduction='mean')
output = loss(input1, input2, target)