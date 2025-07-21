import torch
from torch import nn
from torch.autograd import Variable
p = torch.distributions.Normal(loc=torch.tensor([0.0]), scale=torch.tensor([1.0]))
q = torch.distributions.Normal(loc=torch.tensor([1.0]), scale=torch.tensor([1.0]))
kl_divergence = torch.distributions.kl.kl_divergence(p, q)
kl_divergence = torch.distributions.kl.kl_divergence(q, p)