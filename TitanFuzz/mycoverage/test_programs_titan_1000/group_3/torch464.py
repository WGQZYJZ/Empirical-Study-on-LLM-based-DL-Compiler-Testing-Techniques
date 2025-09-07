import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([(- 1), 0, 1], dtype=torch.float)
output_data = torch.nn.functional.selu(input_data)