import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.Tensor([[2, 3, 4], [5, 6, 7]]))
output = torch.nn.LogSoftmax(dim=1)(input_data)