import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]]], dtype=torch.float32)
pad = torch.nn.ReflectionPad2d((1, 1, 1, 1))
output = pad(input)