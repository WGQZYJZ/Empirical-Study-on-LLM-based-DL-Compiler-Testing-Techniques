import torch
from torch import nn
from torch.autograd import Variable
if torch.distributed.is_available():
    print('Distributed package is available')
else:
    print('Distributed package is NOT available')