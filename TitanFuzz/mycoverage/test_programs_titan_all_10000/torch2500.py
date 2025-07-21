import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 3, 224, 224)
torch.random.initial_seed()
torch.set_grad_enabled(True)
torch.set_grad_enabled(False)
torch.get_num_threads()
torch.set_num_threads(1)
torch.get_num_interop_threads()
torch.set_num_interop_threads(1)