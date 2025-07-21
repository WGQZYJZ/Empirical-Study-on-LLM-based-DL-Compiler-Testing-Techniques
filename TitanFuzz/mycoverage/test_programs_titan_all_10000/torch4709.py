import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.tensor([1, 2, 3, 4, 5])
_output_tensor = torch.Tensor.tile(_input_tensor, dims=2)