import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
inverted_tensor = torch.bitwise_not(input_tensor)