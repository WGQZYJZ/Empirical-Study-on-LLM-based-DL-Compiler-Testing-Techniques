import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randint(10, (2, 3, 4), dtype=torch.float32)
torch.Tensor.log10_(_input_tensor)