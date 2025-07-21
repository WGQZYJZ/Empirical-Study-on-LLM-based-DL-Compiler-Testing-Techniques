'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.kl.kl_divergence\ntorch.distributions.kl.kl_divergence(p, q)\n'
import torch
import torch.distributions.kl as kl
p = torch.distributions.Normal(0, 1)
q = torch.distributions.Normal(0, 2)
kl_divergence = kl.kl_divergence(p, q)
print(kl_divergence)