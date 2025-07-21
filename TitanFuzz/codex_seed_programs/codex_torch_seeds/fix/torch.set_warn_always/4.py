'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_warn_always\ntorch.set_warn_always(b)\n'
import torch
from torch.autograd import Variable
from torch import nn
from torch.nn import functional as F
from torch import optim
x = Variable(torch.ones(2, 2), requires_grad=True)
print(x)
torch.set_warn_always(True)
torch.set_warn_always(False)