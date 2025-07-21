import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randint(1, 10, (3, 3), dtype=torch.float32)
_output_tensor = torch.Tensor.byte(_input_tensor)