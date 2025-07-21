import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randint(0, 2, (3, 3), dtype=torch.int16)
torch.Tensor.bitwise_not_(_input_tensor)