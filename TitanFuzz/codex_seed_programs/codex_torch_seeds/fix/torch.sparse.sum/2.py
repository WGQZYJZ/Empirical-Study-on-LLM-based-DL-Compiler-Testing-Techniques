'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sparse.sum\ntorch.sparse.sum(input, dim=None, dtype=None)\n'
import torch
from torch.autograd import Variable
import torch
input = Variable(torch.sparse.FloatTensor(torch.LongTensor([[0, 1], [1, 0]]), torch.randn(2), torch.Size([2, 2])))
torch.sparse.sum(input, dim=None, dtype=None)