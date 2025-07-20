input = torch.randn(1, 1, 5, 5)
input = torch.randn(1, 1, 5, 5)
output = torch.nn.LocalResponseNorm(size=1, alpha=0.0001, beta=0.75, k=1.0)(input)