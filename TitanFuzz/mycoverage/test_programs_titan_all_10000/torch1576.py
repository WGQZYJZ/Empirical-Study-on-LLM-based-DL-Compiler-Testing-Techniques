import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[1.0, 2.0, 3.0, 4.0, 5.0, 6.0]], dtype=torch.float32)
torch.multinomial(input, 3)
torch.multinomial(input, 3, replacement=True)
torch.multinomial(input, 3, replacement=False)
torch.multinomial(input, 3, replacement=False, out=torch.LongTensor([[0, 0, 0]]))
torch.multinomial(input, 3, replacement=True, out=torch.LongTensor([[0, 0, 0]]))
torch.multinomial(input, 3, replacement=False, out=torch.LongTensor([[0, 0, 0]]))