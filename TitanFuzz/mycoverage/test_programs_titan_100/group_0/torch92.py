import torch
from torch import nn
from torch.autograd import Variable
if True:
    print('PyTorch version: ', torch.__version__)
    input_data = torch.rand(10, 10)
    print('input_data: ', input_data)
    future = torch.futures.Future()