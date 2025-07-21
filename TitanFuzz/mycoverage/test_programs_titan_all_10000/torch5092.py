import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randint(1, 100, (10,))
_output_tensor = torch.Tensor.copy_(_input_tensor, src=torch.randint(1, 100, (10,)))