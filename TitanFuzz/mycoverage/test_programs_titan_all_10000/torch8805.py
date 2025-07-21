import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.tensor([(- 1), (- 2), 3, 4, (- 5), 6])
_output_tensor = torch.Tensor.abs(_input_tensor)
_output_tensor = torch.abs(_input_tensor)