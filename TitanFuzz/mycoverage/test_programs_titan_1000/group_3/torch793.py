import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([(- 3.14), (- 2.14), (- 1.14), 0.14, 1.14, 2.14, 3.14])
output_data = torch.remainder(input_data, 2.0)