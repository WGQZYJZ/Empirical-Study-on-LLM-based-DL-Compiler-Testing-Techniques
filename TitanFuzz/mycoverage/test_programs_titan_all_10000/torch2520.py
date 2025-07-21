import torch
from torch import nn
from torch.autograd import Variable
if True:
    input_data = torch.randn(4, 4)
    print('Input data: ', input_data)
    output_data = torch.conj(input_data)
    print('Output data: ', output_data)