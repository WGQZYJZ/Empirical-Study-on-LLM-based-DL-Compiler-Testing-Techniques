a = torch.randn(4, 2)
b = torch.renorm(a, p=2, dim=1, maxnorm=1)