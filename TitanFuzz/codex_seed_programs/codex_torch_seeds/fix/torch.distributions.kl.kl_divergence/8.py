'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.kl.kl_divergence\ntorch.distributions.kl.kl_divergence(p, q)\n'
import torch
p = torch.distributions.Normal(loc=torch.tensor([0.0]), scale=torch.tensor([1.0]))
q = torch.distributions.Normal(loc=torch.tensor([1.0]), scale=torch.tensor([1.0]))
print(torch.distributions.kl.kl_divergence(p, q))
print(torch.distributions.kl.kl_divergence(p, p))
print(torch.distributions.kl.kl_divergence(q, q))