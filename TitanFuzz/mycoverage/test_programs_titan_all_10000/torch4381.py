import torch
from torch import nn
from torch.autograd import Variable
p = torch.distributions.Categorical(probs=torch.tensor([0.5, 0.5]))
q = torch.distributions.Categorical(probs=torch.tensor([0.6, 0.4]))
kl = torch.distributions.kl.kl_divergence(p, q)