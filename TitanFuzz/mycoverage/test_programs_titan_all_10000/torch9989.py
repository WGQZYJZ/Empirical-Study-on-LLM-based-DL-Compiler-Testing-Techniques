import torch
from torch import nn
from torch.autograd import Variable
input_data = [torch.tensor([3, 10]), torch.tensor([1, 1]), torch.tensor([5])]
packed_sequence = torch.nn.utils.rnn.pack_sequence(input_data)