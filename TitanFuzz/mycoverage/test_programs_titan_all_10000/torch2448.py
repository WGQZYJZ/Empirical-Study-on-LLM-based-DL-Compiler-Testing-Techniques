import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[(- 1), 2, 3], [4, (- 5), 6], [7, 8, (- 9)]])
other = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
torch.Tensor.copysign_(input_tensor, other)