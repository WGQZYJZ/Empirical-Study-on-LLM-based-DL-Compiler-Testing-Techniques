input = torch.randn(2, 3, 4)
output = torch.logcumsumexp(input, dim=1)