x = torch.randn(1, 1, requires_grad=True)
y = torch.special.psi(x)
y.backward()