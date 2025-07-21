import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 3, 3)
torch.nn.functional.sigmoid(input)
torch.nn.functional.relu(input)
torch.nn.functional.tanh(input)
torch.nn.functional.softmax(input, dim=1)
torch.nn.functional.softmax(input, dim=2)
torch.nn.functional.softmax(input, dim=3)
torch