import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.tensor([[10, 15, 20], [25, 30, 35]])
torch.Tensor.gcd_(input_data, 5)