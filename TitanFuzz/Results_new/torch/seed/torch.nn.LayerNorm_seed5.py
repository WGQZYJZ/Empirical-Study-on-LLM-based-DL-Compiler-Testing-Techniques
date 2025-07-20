x = torch.randn(20, 5, 10, 10)
norm = torch.nn.LayerNorm(x.shape[1:])
out = norm(x)