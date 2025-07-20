x = torch.randn(2, 3)
y = torch.renorm(x, p=2, dim=1, maxnorm=1)
y = torch.renorm(x, p=2, dim=1, maxnorm=1.5)