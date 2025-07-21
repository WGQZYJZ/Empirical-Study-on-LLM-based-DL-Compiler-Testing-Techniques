import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randint(low=0, high=100, size=(3, 3), dtype=torch.int)
_gcd_value = torch.Tensor.gcd_(_input_tensor, other=torch.tensor(5))