import torch
from torch import nn
from torch.autograd import Variable
if True:
    print(torch.__version__)
    input_data = torch.arange(1, 13).view(2, 2, 3).float()
    print('Input data:\n', input_data)
    output = torch.rot90(input_data, 1, (1, 2))
    print('Output:\n', output)