import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([(1 + 2j), (3 + 4j), (5 + 6j)])
imag_data = torch.imag(input_data)