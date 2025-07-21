import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.Tensor(3, 5)
input_tensor.uniform_(0, 1)
output_tensor = torch.Tensor.bernoulli_(input_tensor)