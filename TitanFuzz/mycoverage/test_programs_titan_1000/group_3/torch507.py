import torch
from torch import nn
from torch.autograd import Variable
input_size = 2
hidden_size = 2
num_layers = 1
batch_size = 1
input_data = Variable(torch.Tensor([[[1, 2], [3, 4], [5, 6]]]))
lstm = torch.nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
(out, _) = lstm(input_data)