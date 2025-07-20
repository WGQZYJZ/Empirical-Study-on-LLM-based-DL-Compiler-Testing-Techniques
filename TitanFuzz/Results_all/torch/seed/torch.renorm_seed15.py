input = torch.randn(2, 5)
output1 = torch.renorm(input, p=2, dim=1, maxnorm=1)
output2 = torch.renorm(input, p=2, dim=0, maxnorm=1)