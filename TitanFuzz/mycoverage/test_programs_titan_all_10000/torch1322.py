import torch
from torch import nn
from torch.autograd import Variable
input = torch.randint(0, 10, (5, 3, 4))
lengths = torch.tensor([3, 2, 1, 1, 1])
packed_input = torch.nn.utils.rnn.pack_padded_sequence(input, lengths, batch_first=True)