input = torch.randn(3, 5, 5)
tau = torch.randn(3, 5)
other = torch.randn(3, 5, 5)
torch.ormqr(input, tau, other, left=True, transpose=False, out=None)