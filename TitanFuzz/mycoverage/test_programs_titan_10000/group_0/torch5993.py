import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.rand(2, 3, 4)
torch.Tensor.new_empty(input_tensor, size=(2, 3, 4))