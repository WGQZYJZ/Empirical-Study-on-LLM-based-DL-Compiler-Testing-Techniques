input = torch.randn(3, 3)
tau = torch.randn(3)
output = torch.orgqr(input, tau)