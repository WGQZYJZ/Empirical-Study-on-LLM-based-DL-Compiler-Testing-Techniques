input = torch.randn(2, 3)
output = torch.logcumsumexp(input, dim=1)
output = torch.logcumsumexp(input, dim=1, out=input)