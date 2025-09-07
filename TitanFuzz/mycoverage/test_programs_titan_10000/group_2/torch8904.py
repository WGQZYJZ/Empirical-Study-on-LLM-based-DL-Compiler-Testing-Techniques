import torch
from torch import nn
from torch.autograd import Variable

tensor_a = torch.rand(3, 3)
tensor_b = torch.rand(3, 3)
tensor_c = torch.mul(tensor_a, tensor_b)