import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.arange(0, 10)
indices = torch.tensor([0, 2, 4, 6, 8])
output_tensor = torch.Tensor.take(input_tensor, indices)