import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([(- 1.0), (- 0.5), 0.0, 0.5, 1.0])
output_tensor = torch.frexp(input_tensor)