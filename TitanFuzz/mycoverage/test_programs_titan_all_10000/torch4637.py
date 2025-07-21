import torch
from torch import nn
from torch.autograd import Variable
input_data = [torch.tensor([1, 2, 3, 4]), torch.tensor([1, 2]), torch.tensor([1, 2, 3])]
padded_input_data = torch.nn.utils.rnn.pad_sequence(input_data, batch_first=False, padding_value=0.0)