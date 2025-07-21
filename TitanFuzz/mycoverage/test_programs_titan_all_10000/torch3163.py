import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([[1, 2, 3], [4, 5, 0], [6, 0, 0]])
lengths = [3, 2, 1]
packed_x = torch.nn.utils.rnn.pack_padded_sequence(x, lengths, batch_first=True)