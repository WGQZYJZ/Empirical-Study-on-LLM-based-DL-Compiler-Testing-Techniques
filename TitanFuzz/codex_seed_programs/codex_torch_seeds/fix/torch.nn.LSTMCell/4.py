'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LSTMCell\ntorch.nn.LSTMCell(input_size, hidden_size, bias=True, device=None, dtype=None)\n'
import torch
from torch import nn
from torch.autograd import Variable
import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(3, 3))
hx = Variable(torch.randn(3, 3))
cx = Variable(torch.randn(3, 3))
lstm = nn.LSTMCell(3, 3)
output = []
for i in range(5):
    (hx, cx) = lstm(input, (hx, cx))
    output.append(hx)