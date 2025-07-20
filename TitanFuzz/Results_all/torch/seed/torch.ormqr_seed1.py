input = torch.randn(4, 4)
tau = torch.randn(4)
other = torch.randn(4, 4)
out = torch.ormqr(input, tau, other, left=True, transpose=False)