input = torch.randn(3, 4)
output = torch.logcumsumexp(input, dim=1)