import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randint(0, 10, (3, 3))
torch.Tensor.fix_(_input_tensor)