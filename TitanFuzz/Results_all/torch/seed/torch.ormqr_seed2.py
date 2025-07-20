input = torch.randn(3, 4, 4, dtype=torch.float64)
tau = torch.randn(3, 4, dtype=torch.float64)
other = torch.randn(3, 4, 4, dtype=torch.float64)
output = torch.ormqr(input, tau, other, left=True, transpose=False)