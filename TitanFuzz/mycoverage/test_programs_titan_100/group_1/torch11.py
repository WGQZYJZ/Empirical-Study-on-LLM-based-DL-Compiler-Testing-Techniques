import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.tensor([[(- 1.0), 2.0, (- 3.0), 4.0], [5.0, (- 6.0), 7.0, (- 8.0)]])
_result = torch.Tensor.is_signed(_input_tensor)