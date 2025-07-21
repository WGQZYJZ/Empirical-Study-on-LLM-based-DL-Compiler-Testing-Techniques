import torch

input = Variable(torch.randn(1, 3))
output = torch.abs(input)