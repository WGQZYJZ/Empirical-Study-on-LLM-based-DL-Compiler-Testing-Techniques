import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.tensor([[1.5, 2.5, 3.5, 4.5], [5.5, 6.5, 7.5, 8.5], [9.5, 10.5, 11.5, 12.5]])
_output_tensor = torch.Tensor.trunc(_input_tensor)