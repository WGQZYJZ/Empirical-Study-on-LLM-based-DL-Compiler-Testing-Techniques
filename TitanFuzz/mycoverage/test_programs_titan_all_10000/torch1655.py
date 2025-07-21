import torch
from torch import nn
from torch.autograd import Variable
input_size = 5
hidden_size = 3
input = torch.randn(6, 3, input_size)
hx = torch.randn(3, hidden_size)
cx = torch.randn(3, hidden_size)
lstm = torch.nn.LSTMCell(input_size, hidden_size)
for i in range(6):
    (hx, cx) = lstm(input[i], (hx, cx))
    print(hx)
    print(cx)
    print('\n')