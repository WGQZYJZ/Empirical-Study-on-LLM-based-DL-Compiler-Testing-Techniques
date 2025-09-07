import torch
from torch import nn
from torch.autograd import Variable
if True:
    input_data = torch.rand(1, 2, 3, 4)
    print(input_data)
    print(input_data.shape)
    output_data = torch.rand_like(input_data)
    print(output_data)
    print(output_data.shape)