import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[1, 2, 4, 5], [4, 3, 2, 9]])
weight = torch.randn(10, 3)
embedding = torch.nn.functional.embedding(input, weight)