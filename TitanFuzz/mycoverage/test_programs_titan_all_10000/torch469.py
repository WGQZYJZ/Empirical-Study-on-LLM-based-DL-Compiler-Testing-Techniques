import torch
from torch import nn
from torch.autograd import Variable
a = torch.rand(10000, 10000)
b = torch.rand(10000, 10000)
torch.set_num_threads(4)
start = time.time()
c = torch.mm(a, b)
end = time.time()