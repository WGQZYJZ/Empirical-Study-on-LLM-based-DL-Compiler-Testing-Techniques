input = torch.randn(2, 5)
output = torch.renorm(input, p=2, dim=1, maxnorm=1)