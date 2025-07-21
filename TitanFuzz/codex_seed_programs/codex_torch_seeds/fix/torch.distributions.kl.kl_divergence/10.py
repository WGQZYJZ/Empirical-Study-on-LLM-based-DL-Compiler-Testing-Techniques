'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.kl.kl_divergence\ntorch.distributions.kl.kl_divergence(p, q)\n'
import torch
from torch.distributions import MultivariateNormal
from torch.distributions.kl import kl_divergence
mu_p = torch.tensor([0.0, 0.0])
cov_p = torch.tensor([[1.0, 0.0], [0.0, 1.0]])
p = MultivariateNormal(mu_p, cov_p)
mu_q = torch.tensor([1.0, 1.0])
cov_q = torch.tensor([[1.0, 0.0], [0.0, 1.0]])
q = MultivariateNormal(mu_q, cov_q)
print(kl_divergence(p, q))
print(kl_divergence(q, p))
print(kl_divergence(q, q))
print(kl_divergence(p, p))
mu_p = torch.tensor([0.0, 0.0])
cov_p = torch.tensor