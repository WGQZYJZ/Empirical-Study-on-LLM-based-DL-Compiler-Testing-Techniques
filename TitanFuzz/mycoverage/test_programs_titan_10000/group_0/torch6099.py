import torch
from torch import nn
from torch.autograd import Variable

_input_tensor = torch.tensor([[(- 1), (- 2), (- 3)], [1, 2, 3]])
torch.Tensor.sigmoid_(_input_tensor)