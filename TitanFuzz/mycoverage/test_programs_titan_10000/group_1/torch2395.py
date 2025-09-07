import torch
from torch import nn
from torch.autograd import Variable

x = torch.ones(2, 2)
y = torch.ones(2, 2)
torch.set_num_threads(4)
start = time.time()
for i in range(100):
    z = (x + y)
end = time.time()