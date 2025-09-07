import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
other = torch.tensor([2.0, 2.0, 2.0, 2.0, 2.0, 2.0])
output_tensor = torch.Tensor.less_(input_tensor, other)