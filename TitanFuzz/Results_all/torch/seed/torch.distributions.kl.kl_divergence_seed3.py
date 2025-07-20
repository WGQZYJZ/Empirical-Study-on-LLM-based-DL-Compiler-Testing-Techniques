p = torch.distributions.Normal(0.0, 1.0)
q = torch.distributions.Normal(1.0, 1.0)
kl = torch.distributions.kl.kl_divergence(p, q)