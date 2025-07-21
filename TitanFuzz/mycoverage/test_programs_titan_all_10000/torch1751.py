import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 10)
torch.Generator(device='cpu')
torch.Generator.manual_seed(generator=None, seed=0)
torch.Generator.initial_seed(generator=None)
torch.Generator.seed(generator=None)
torch.Generator.get_state(generator=None)
torch.Generator.set_state(generator=None, state=None)
torch.Generator.state_dict(generator=None)