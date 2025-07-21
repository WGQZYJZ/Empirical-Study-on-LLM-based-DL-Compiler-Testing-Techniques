import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([(- 2.0), (- 1.0), 0.0, 1.0, 2.0])
output = torch.nn.functional.softshrink(input_data, lambd=0.5)