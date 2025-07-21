import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3, 4, 5)
output_data = torch.nn.functional.relu6(input_data)