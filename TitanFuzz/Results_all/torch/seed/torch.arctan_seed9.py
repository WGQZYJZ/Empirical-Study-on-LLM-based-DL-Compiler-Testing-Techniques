x = torch.randn(1, requires_grad=True)
y = torch.arctan(x)
y.backward()