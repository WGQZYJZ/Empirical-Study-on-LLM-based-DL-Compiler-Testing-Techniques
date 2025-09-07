import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.tensor([0, 1, 1, 2, 2, 2, 3, 3, 3, 3])
_result_tensor = torch.Tensor.bincount(_input_tensor)