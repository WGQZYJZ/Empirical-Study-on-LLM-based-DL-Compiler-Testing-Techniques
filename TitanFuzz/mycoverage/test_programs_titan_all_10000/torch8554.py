import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randint(low=0, high=2, size=(4, 4), dtype=torch.int8)
torch.Tensor.bitwise_not(_input_tensor)