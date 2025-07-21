import torch
from torch import nn
from torch.autograd import Variable
x1 = torch.tensor([[1, 2, 3], [4, 5, 6]])
x2 = torch.tensor([[7, 8, 9], [10, 11, 12]])
x3 = torch.tensor([[13, 14, 15], [16, 17, 18]])
x = torch.nn.utils.rnn.pad_sequence([x1, x2, x3])