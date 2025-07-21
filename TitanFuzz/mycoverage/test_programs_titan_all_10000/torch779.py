import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(1, 3, 224, 224)
torch.Tensor.new_ones(input_tensor, (1, 3, 224, 224))