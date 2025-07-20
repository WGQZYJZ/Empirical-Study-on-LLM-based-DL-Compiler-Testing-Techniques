x = torch.randn(1, 1, requires_grad=True)
y = torch.special.digamma(x)
y.backward()