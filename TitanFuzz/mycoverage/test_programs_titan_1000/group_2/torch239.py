import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([(- 1.0), (- 0.5), 0, 0.5, 1.0])
softsign = torch.nn.Softsign()
output_data = softsign(input_data)