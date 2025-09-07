import torch
from torch import nn
from torch.autograd import Variable

data = np.random.rand(100, 100)
num_threads = torch.get_num_interop_threads()