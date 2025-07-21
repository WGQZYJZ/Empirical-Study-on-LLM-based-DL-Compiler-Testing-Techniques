import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[1, 2, 3], [4, 5, 0], [6, 0, 0]], dtype=torch.float32)
lengths = torch.tensor([3, 2, 1], dtype=torch.int32)
packed_input = torch.nn.utils.rnn.pack_padded_sequence(input_data, lengths, batch_first=False, enforce_sorted=True)
(padded_input, lengths) = torch.nn.utils.rnn.pad_packed_sequence(packed_input, batch_first=False)