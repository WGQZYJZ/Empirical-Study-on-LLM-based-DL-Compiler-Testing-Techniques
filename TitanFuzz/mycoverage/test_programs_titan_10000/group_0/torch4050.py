import torch
from torch import nn
from torch.autograd import Variable

input_data = [i for i in range(10)]
sampler = torch.utils.data.SequentialSampler(input_data)