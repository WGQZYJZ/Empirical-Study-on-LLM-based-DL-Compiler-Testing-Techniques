import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.Tensor([[[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]]))
output = torch.nn.AdaptiveMaxPool2d(output_size=(2, 2))(input)