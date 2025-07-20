input = Variable(torch.randn(1, 1, 10, 10))
lrn = torch.nn.LocalResponseNorm(size=2, alpha=0.0001, beta=0.75, k=1.0)
output = lrn(input)