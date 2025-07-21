'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.kl.kl_divergence\ntorch.distributions.kl.kl_divergence(p, q)\n'
import torch
p = torch.distributions.Normal(0.0, 1.0)
q = torch.distributions.Normal(1.0, 1.0)
kl = torch.distributions.kl.kl_divergence(p, q)
print(kl)