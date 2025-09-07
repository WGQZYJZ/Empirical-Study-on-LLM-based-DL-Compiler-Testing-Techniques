import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.arange((- 5), 5, 0.1)
output_data = torch.nn.functional.relu_(input_data)