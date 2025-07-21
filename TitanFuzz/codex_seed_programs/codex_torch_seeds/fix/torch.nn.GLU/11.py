'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GLU\ntorch.nn.GLU(dim=-1)\n'
import torch
from torch.autograd import Variable
x = Variable(torch.Tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), requires_grad=True)
glu = torch.nn.GLU()
y = glu(x)
print(y)
'\ntorch.nn.GRU(input_size, hidden_size, num_layers=1, bias=True, batch_first=False, dropout=0, bidirectional=False)\n'
input = Variable(torch.randn(5, 3, 10))
h0 = Variable(torch.randn(2, 3, 20))
gru = torch.nn.GRU(10, 20, 2)
(out, hn) = gru(input, h0)
print(out)
print(hn)