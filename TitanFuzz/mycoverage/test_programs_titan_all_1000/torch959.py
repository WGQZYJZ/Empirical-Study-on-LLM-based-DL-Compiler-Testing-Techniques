import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.Tensor([[1.0, (- 1.0), (- 1.0), 1.0]]))
target = Variable(torch.LongTensor([0]))
hinge_loss = torch.nn.HingeEmbeddingLoss()
output = hinge_loss(input, target)