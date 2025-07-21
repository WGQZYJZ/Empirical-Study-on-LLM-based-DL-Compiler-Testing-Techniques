import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor(data=[(- 1.0), 1.0, (- 1.0), 1.0], requires_grad=True)
torch.nn.utils.clip_grad_value_(x, 0.5)