import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randint(1, 10, (2, 3, 4))
shifts = torch.tensor([1, 2])
dims = torch.tensor([0, 1])
output_tensor = torch.Tensor.roll(_input_tensor, shifts, dims)