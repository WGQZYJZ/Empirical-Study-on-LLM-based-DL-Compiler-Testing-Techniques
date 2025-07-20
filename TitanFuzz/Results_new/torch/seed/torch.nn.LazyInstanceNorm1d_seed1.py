x = torch.randn(1, 2, 3)
norm = torch.nn.LazyInstanceNorm1d(2)
y = norm(x)