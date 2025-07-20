input = torch.randn(2, dtype=torch.float, requires_grad=True)
output = torch.special.digamma(input)