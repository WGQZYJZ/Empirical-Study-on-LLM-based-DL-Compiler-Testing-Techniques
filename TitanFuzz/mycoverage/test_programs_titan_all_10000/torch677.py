import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([1.0])
sigmoid = torch.nn.Sigmoid()
output = sigmoid(input)