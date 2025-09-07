import torch
from torch import nn
from torch.autograd import Variable

x = torch.rand(10000, 10000)
torch.set_num_threads(4)
start = time.time()
y = torch.mm(x, x)
end = time.time()