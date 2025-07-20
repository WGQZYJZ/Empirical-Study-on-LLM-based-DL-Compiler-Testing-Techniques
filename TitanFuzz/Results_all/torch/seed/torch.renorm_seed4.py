input = torch.randn(4, 4)
output = torch.renorm(input, p=2, dim=0, maxnorm=1)