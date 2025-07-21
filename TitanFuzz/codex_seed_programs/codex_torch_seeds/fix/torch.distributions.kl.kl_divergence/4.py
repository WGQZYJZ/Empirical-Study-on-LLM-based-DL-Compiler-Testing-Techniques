'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.kl.kl_divergence\ntorch.distributions.kl.kl_divergence(p, q)\n'
import torch
p = torch.distributions.Categorical(probs=torch.tensor([0.5, 0.5]))
q = torch.distributions.Categorical(probs=torch.tensor([0.6, 0.4]))
kl = torch.distributions.kl.kl_divergence(p, q)
print(kl)