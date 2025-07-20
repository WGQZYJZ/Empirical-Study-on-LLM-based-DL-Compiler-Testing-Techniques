input = torch.randn(3, 4)
output = torch.logsumexp(input, dim=1)