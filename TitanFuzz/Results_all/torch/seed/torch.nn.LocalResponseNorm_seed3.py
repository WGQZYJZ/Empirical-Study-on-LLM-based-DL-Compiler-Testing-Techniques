input = Variable(torch.randn(1, 3, 5, 5))
lrn = torch.nn.LocalResponseNorm(size=5, alpha=0.0001, beta=0.75, k=1.0)
output = lrn(input)