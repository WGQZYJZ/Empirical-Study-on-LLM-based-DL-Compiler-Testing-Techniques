x = torch.randn(1, 1, requires_grad=True)
y = torch.nn.Softplus()(x)
y.backward()