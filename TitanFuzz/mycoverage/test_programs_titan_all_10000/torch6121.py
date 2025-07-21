import torch
from torch import nn
from torch.autograd import Variable
data = [torch.tensor([1, 2, 3, 4]), torch.tensor([5, 6, 7]), torch.tensor([8, 9])]
padded_data = torch.nn.utils.rnn.pad_sequence(data, padding_value=0)