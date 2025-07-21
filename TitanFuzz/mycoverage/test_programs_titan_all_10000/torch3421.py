import torch
from torch import nn
from torch.autograd import Variable
input_data = [torch.randn(1, 3), torch.randn(2, 3), torch.randn(3, 3)]
output_data = torch.nn.utils.rnn.pad_sequence(input_data, batch_first=True)