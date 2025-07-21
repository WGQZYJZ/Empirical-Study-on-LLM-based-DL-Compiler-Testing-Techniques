import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.arange(0, 10)
(train_data, test_data) = torch.utils.data.random_split(input_data, [5, 5])