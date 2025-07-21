import torch
from torch import nn
from torch.autograd import Variable
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data_qint8 = torch.QInt8Storage(data)