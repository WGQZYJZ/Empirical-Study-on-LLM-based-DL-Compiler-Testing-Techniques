'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.kl.kl_divergence\ntorch.distributions.kl.kl_divergence(p, q)\n'
import torch
from torch.distributions import Normal
mu1 = torch.tensor([0.0])
mu2 = torch.tensor([1.0])
sigma1 = torch.tensor([1.0])
sigma2 = torch.tensor([1.0])
p = Normal(loc=mu1, scale=sigma1)
q = Normal(loc=mu2, scale=sigma2)
kl_divergence = torch.distributions.kl.kl_divergence(p, q)
print(kl_divergence)