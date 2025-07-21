import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])
other_tensor = torch.tensor([2.0, 2.0, 2.0, 2.0, 2.0])
output_tensor = torch.Tensor.subtract_(input_tensor, other_tensor)