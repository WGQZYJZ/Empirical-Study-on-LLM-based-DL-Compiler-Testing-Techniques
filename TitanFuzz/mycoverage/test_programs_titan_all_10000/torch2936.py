import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randint(1, 10, (2, 3), dtype=torch.int)
_lcm_result = torch.Tensor.lcm(_input_tensor, _input_tensor)