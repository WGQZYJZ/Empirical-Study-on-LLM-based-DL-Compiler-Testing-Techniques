x = torch.randn(3, 3, requires_grad=True)
y = torch.cholesky_inverse(x)