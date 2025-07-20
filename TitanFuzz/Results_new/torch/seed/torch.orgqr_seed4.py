input = torch.randn(2, 3, 3)
tau = torch.randn(2, 3)
output = torch.orgqr(input, tau)