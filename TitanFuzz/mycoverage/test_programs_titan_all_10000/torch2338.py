import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.randn(5, 3))
seq = torch.nn.Sequential(torch.nn.Linear(3, 5), torch.nn.ReLU(), torch.nn.Linear(5, 2), torch.nn.ReLU())
output = seq.forward(input_data)
for param in seq.parameters():
    print(param)