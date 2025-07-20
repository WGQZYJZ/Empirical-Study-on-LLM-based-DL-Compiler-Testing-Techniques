x = torch.randn(1, requires_grad=True)
y = torch.exp(x)
y.backward()