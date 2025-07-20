input = torch.randn(2, 2)
tau = torch.randn(2)
(q, r) = torch.orgqr(input, tau)