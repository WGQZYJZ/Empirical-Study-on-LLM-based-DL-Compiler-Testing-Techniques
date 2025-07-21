import torch
from torch import nn
from torch.autograd import Variable
data_1 = torch.Tensor(2, 3)
data_2 = torch.Tensor(2, 3)
data_3 = torch.add(data_1, data_2)
data_4 = torch.add(data_1, data_2, out=data_3)
data_5 = torch.add(data_1, data_2, alpha=2)
data_6 = torch.add(data_1, data_2, alpha=2, out=data_5)