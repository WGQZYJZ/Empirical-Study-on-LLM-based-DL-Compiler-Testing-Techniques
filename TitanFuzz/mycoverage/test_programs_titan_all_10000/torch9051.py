import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(1, 3, 3)
output_tensor = torch.Tensor.new_full(_input_tensor, size=[1, 3, 3], fill_value=1)