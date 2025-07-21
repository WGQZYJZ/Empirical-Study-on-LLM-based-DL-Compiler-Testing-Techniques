import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(1, 1)
input
torch.poisson(input, generator=None)
new_generator = torch.Generator()
new_generator.manual_seed(12345)
torch.poisson(input, generator=new_generator)
new_generator = torch.Generator()
new_generator.manual_seed(12346)
torch.poisson(input, generator=new_generator)
new_generator = torch.Generator()
new_generator.manual_seed(12347)
torch.poisson(input, generator=new_generator)